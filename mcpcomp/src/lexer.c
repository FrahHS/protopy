#include "lexer.h"

// Token types

const char* token_type_to_string(TokenType type) {
    switch(type) {
        case PARENTHESIS_OPEN:      return "PARENTHESIS_OPEN";
        case PARENTHESIS_CLOSE:     return "PARENTHESIS_CLOSE";
        case BRACKET_OPEN:          return "BRACKET_OPEN";
        case BRACKET_CLOSE:         return "BRACKET_CLOSE";
        case DATATYPE:              return "DATATYPE";
        case SEMICOLON:             return "SEMICOLON";
        case EQUAL:                 return "EQUAL";
        case LINE_COMMENT:          return "LINE_COMMENT";
        case IDENTIFIER:            return "IDENTIFIER";
        case PACKETSTATE:           return "PACKETSTATE";
        case PACKETBOUND:           return "PACKETBOUND";
        case STRING_LITERAL:        return "STRING_LITERAL";
        case INT_LITERAL:           return "INT_LITERAL";
        case BYTE_LITERAL:          return "BYTE_LITERAL";
        case HEADER:                return "HEADER";
        case PACKET:                return "PACKET";
        case FALSE:                 return "FALSE";
        case TRUE:                  return "TRUE";
        case END:                   return "END";

        default: return "UNKNOWN";
    }
}

void lexer_print_error(Lexer *l, char *message, ...) {
    printf(
        RED "%s(%d,%d): %s.\n" RESET,
        l->filename,
        l->line,
        l->col,
        message
    );
}

TokenType lexer_get_keyword(char *literal) {
    if(datatype_is_keyword_supported_general(literal))  return DATATYPE;
    if(packet_state_is_supported_general(literal))      return PACKETSTATE;
    if(packet_bound_is_supported_general(literal))      return PACKETBOUND;
    else if(strcmp(literal, "Header") == 0)             return HEADER;
    else if(strcmp(literal, "Packet") == 0)             return PACKET;
    else if(strcmp(literal, "True") == 0)               return TRUE;
    else if(strcmp(literal, "False") == 0)              return FALSE;

    return UNKNOWN;
}

int lexer_is_keyword(char *literal) {
    return lexer_get_keyword(literal) != UNKNOWN;
}

void token_print(Token token) {
    printf("MCPC Token at (%d, %d):\n", token.line, token.col);
    printf("Token Type: %s\n", token_type_to_string(token.type));
    printf("Token Literal: %s\n", token.literal ? token.literal : "(null)");
    printf("\n");
}

char lexer_peek_char(Lexer *l) {
    if(l->read_pos >= l->buffer_len) {
        return EOF;
    }

    return l->buffer[l->read_pos];
}

char lexer_read_char(Lexer *l) {
    l->ch = lexer_peek_char(l);

    l->pos = l->read_pos;
    l->read_pos += 1;
    l->col += 1;

    return l->ch;
}

int lexer_match_next(Lexer *l, char c) {
    if(lexer_peek_char(l) != c) {
        return 0;
    }

    lexer_read_char(l);
    return 1;
}

void lexer_init(Lexer *l, char *filename,char *buffer, unsigned long buffer_len) {
    l->filename = filename;
    l->buffer = buffer;
    l->buffer_len = buffer_len;
    l->pos = 0;
    l->read_pos = 0;
    l->ch = 0;
    l->line = 1;
    l->col = 0;

    lexer_read_char(l);
}

void lexer_skip_whitespace(Lexer *l) {
    if(l->ch == ' ') {
        lexer_read_char(l);
        lexer_skip_whitespace(l);
    } else if(l->ch == '\n') {
        l->col = 0;
        l->line++;
        lexer_read_char(l);
        lexer_skip_whitespace(l);
    } else if(l->ch == '\t') {
        lexer_read_char(l);
        lexer_skip_whitespace(l);
    }
}

void lexer_skip_comment(Lexer *l) {
    if(l->ch == '/' && lexer_match_next(l, '/')) {
        while(l->ch != '\n' && l->ch != EOF) {
            lexer_read_char(l);
        }
    }
}

Token lexer_generate_token(Lexer *l, TokenType type, char *literal) {

    // TODO: line and col could be wrong
    return (Token) {
        .type = type,
        .literal = _strdup(literal),
        .line = l->line,
        .col = l->col - (literal == NULL ? 0 : (int) strlen(literal) )
    };
}

Token lexer_string(Lexer *l) {
    char literal[MAX_STR_LEN];
    literal[0] = '\0';

    append_char(literal, l->ch);
    lexer_read_char(l);
    while(l->ch != '"' && l->ch != EOF) {
        if(l->ch == '\n') {
            l->line++;
        }
        append_char(literal, l->ch);
        lexer_read_char(l);
    }

    if(lexer_peek_char(l) == EOF) {
        lexer_print_error(l, "Unterminated string.");
    }

    // The closing ".
    append_char(literal, l->ch);
    lexer_read_char(l);

    // Trim the surrounding quotes.
    return lexer_generate_token(l, STRING_LITERAL, literal);
}

Token lexer_number(Lexer *l) {
    char literal[MAX_STR_LEN];
    literal[0] = '\0';

    while(isdigit(l->ch)) {
        append_char(literal, l->ch);
        lexer_read_char(l);
    }

    // Look for a fractional part.
    if(l->ch == '.' && isdigit(lexer_peek_char(l))) {
        // Consume the "."
        append_char(literal, l->ch);
        lexer_read_char(l);

        while(isdigit(l->ch)) {
            append_char(literal, l->ch);
            lexer_read_char(l);
        }

        return lexer_generate_token(l, DOUBLE_LITERAL, literal);
    }

    return lexer_generate_token(l, INT_LITERAL, literal);
}

Token lexer_byte(Lexer *l) {
    char literal[MAX_STR_LEN];
    literal[0] = '\0';

    while(isalnum(l->ch)) {
        append_char(literal, l->ch);
        lexer_read_char(l);
    }

    return lexer_generate_token(l, BYTE_LITERAL, literal);
}

Token lexer_identifier(Lexer *l) {
    char literal[MAX_STR_LEN];
    literal[0] = '\0';

    while(isalnum(l->ch) || l->ch == '_') {
        append_char(literal, l->ch);
        lexer_read_char(l);
    }

    // Check if current string is a reserved keyword.
    if(lexer_is_keyword(literal)) {
        return lexer_generate_token(l, lexer_get_keyword(literal), literal);
    }

    return lexer_generate_token(l, IDENTIFIER, literal);
}

Token lexer_next_token(Lexer *l) {
    lexer_skip_whitespace(l);
    lexer_skip_comment(l);

    switch(l->ch) {
        case EOF: lexer_read_char(l); return lexer_generate_token(l, END,               " ");
        case '(': lexer_read_char(l); return lexer_generate_token(l, PARENTHESIS_OPEN,  "(");
        case ')': lexer_read_char(l); return lexer_generate_token(l, PARENTHESIS_CLOSE, ")");
        case '{': lexer_read_char(l); return lexer_generate_token(l, BRACKET_OPEN,      "{");
        case '}': lexer_read_char(l); return lexer_generate_token(l, BRACKET_OPEN,      "}");
        case ';': lexer_read_char(l); return lexer_generate_token(l, SEMICOLON,         ";");
        case '=': lexer_read_char(l); return lexer_generate_token(l, EQUAL,             "=");

        case '"': return lexer_string(l);
        case '0': if(lexer_peek_char(l) == 'x') return lexer_byte(l);

        default:
            if(isdigit(l->ch)) {
                return lexer_number(l);
            } else if(isalnum(l->ch) || l->ch == '_') {
                return lexer_identifier(l);
            }

            lexer_print_error(l, "Unexpected character");
            return lexer_generate_token(l, UNKNOWN, NULL);
    }
}

int lexer_tokenize(char *buffer, char *filename, unsigned long length, DynamicArray *tokens) {
    Lexer l;
    lexer_init(&l, filename, buffer, length);

    Token token;
    do {
        token = lexer_next_token(&l);
        dynamic_array_append(tokens, &token);
    } while(token.type != END);

    return 0;
}
