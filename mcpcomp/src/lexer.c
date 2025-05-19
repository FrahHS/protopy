#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#include "lexer.h"

const char* token_type_to_string(TokenType type) {
    switch(type) {
        case ARRAY:
            return "ARRAY";
        case ASSIGN:
            return "ASSIGN";
        case BYTE:
            return "BYTE";
        case BYTE_LITERAL:
            return "BYTE_LITERAL";
        case BOOL:
            return "BOOL";
        case BOOL_LITERAL:
            return "BOOL_LITERAL";
        case BRACKET_CLOSE:
            return "BRACKET_CLOSE";
        case BRACKET_OPEN:
            return "BRACKET_OPEN";
        case COUNT:
            return "COUNT";
        case END:
            return "END";
        case HEADER:
            return "HEADER";
        case INT:
            return "INT";
        case INT_LITERAL:
            return "INT_LITERAL";
        case LINE_COMMENT:
            return "LINE_COMMENT";
        case OPTIONAL:
            return "OPTIONAL";
        case PACKET:
            return "PACKET";
        case PARENTHESIS_CLOSE:
            return "PARENTHESIS_CLOSE";
        case PARENTHESIS_OPEN:
            return "PARENTHESIS_OPEN";
        case SEMICOLON:
            return "SEMICOLON";
        case STRING:
            return "STRING";
        case STRING_LITERAL:
            return "STRING_LITERAL";
        case UUID:
            return "UUID";
        case UNKNOWN:
            return "UNKNOWN";
        case VARINT:
            return "VARINT";
        default:
            return "UNKNOWN";
    }
}

Token literal_to_token(char *literal) {
    if(strcmp(literal, "Header") == 0) {
        return (Token){.type = HEADER, .value = NULL};
    } else if(strcmp(literal, "Array") == 0) {
        return (Token){.type = ARRAY, .value = NULL};
    } else if(strcmp(literal, "Packet") == 0) {
        return (Token){.type = PACKET, .value = NULL};
    } else if(strcmp(literal, "Optional") == 0) {
        return (Token){.type = OPTIONAL, .value = NULL};
    } else if(strcmp(literal, "String") == 0) {
        return (Token){.type = STRING, .value = NULL};
    } else if(strcmp(literal, "UUID") == 0) {
        return (Token){.type = UUID, .value = NULL};
    } else if(strcmp(literal, "Bool") == 0) {
        return (Token){.type = BOOL, .value = NULL};
    } else if(strcmp(literal, "VarInt") == 0) {
        return (Token){.type = VARINT, .value = NULL};
    } else if(strcmp(literal, "True") == 0) {
        return (Token){.type = BOOL_LITERAL, .value = literal};
    } else if(strcmp(literal, "False") == 0) {
        return (Token){.type = BOOL_LITERAL, .value = literal};
    } else {
        return (Token){.type = STRING_LITERAL, .value = _strdup(literal)};
    }
}

int lexer_is_space(char c) {
    switch(c) {
        case ' ':
            return 1;
        case '\n':
            return 1;
    }

    return 0;
}

void lexer_print_token(Token token) {
    printf("MCPC Token:\n");
    printf("Token Type: %s\n", token_type_to_string(token.type));
    printf("Token value: %s\n\n", token.value ? token.value : "(null)");
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

    return l->ch;
}

void lexer_skip_whitespace(Lexer *l) {
    while(lexer_is_space(l->ch)) {
        if(l->ch == ' ') {
            l->col++;
        } else if(l->ch == '\n') {
            l->col = 0;
            l->line++;
        }
        lexer_read_char(l);
    }
}

void lexer_init(Lexer *l, char *buffer, unsigned long buffer_len) {
    l->buffer = buffer;
    l->buffer_len = buffer_len;
    l->pos = 0;
    l->read_pos = 0;
    l->ch = 0;

    lexer_read_char(l);
}

Token lexer_next_token(Lexer *l) {
    lexer_skip_whitespace(l);

    // KEYWORD
    if (l->ch == EOF) {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = END, .value = NULL};
    } else if (l->ch == '(') {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = PARENTHESIS_OPEN, .value = NULL};
    } else if (l->ch == ')') {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = PARENTHESIS_CLOSE, .value = NULL};
    } else if (l->ch == '{') {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = BRACKET_OPEN, .value = NULL};
    } else if (l->ch == '}') {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = BRACKET_CLOSE, .value = NULL};
    } else if (l->ch == ';') {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = SEMICOLON, .value = NULL};
    } else if (l->ch == '=') {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = ASSIGN, .value = NULL};
    }
 
    // BYTE/INTEGER LITERAL
    else if (isdigit(l->ch)) {
        char value[MAX_STR_LEN];
        value[0] = '\0';

        // BYTE
        if(l->ch == '0') {
            append_char(value, l->ch);
            lexer_read_char(l);
            if(l->ch == 'x') {
                while (isalnum(l->ch) || l->ch == '_') {
                    append_char(value, l->ch);
                    lexer_read_char(l);
                }

                l->col += strlen(value);
                return (Token){.type = BYTE_LITERAL, .value = _strdup(value)};
            }
        }

        // INTEGER
        while (isdigit(l->ch)) {
            append_char(value, l->ch);
            lexer_read_char(l);
        }

        l->col += strlen(value);
        return (Token){.type = INT_LITERAL, .value = _strdup(value)};
    }

    // STRING LITERAL
    else if (isalnum(l->ch) || l->ch == '_') {
        char value[MAX_STR_LEN];
        value[0] = '\0';

        while (isalnum(l->ch) || l->ch == '_') {
            append_char(value, l->ch);
            lexer_read_char(l);
        }

        // Check if current string is a reserved keyword.
        l->col += strlen(value);
        return literal_to_token(value);
    } 

    // UNKNOWN
    else {
        lexer_read_char(l);
        l->col++;
        return (Token){.type = UNKNOWN, .value = NULL};
    }
}

int lexer_tokenize(char *buffer, unsigned long length, DynamicArray *tokens) {
    Lexer l;
    lexer_init(&l, buffer, length);

    Token token;
    do {
        token = lexer_next_token(&l);
        token.line = l.line;
        token.col = l.col;
        dynamic_array_append(tokens, &token);
    } while(token.type != END);

    return 0;
}
