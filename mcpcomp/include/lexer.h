#ifndef LEXER_H
#define LEXER_H

#include "util.h"

typedef enum {
    ARRAY,
    ASSIGN,
    BYTE,
    BYTE_LITERAL,
    BOOL,
    BOOL_LITERAL,
    BRACKET_CLOSE,
    BRACKET_OPEN,
    COUNT,
    END,
    HEADER,
    INT,
    INT_LITERAL,
    LINE_COMMENT,
    OPTIONAL,
    PACKET,
    PARENTHESIS_CLOSE,
    PARENTHESIS_OPEN,
    SEMICOLON,
    STRING,
    STRING_LITERAL,
    UUID,
    UNKNOWN,
    VARINT
} KeyWord;

typedef struct {
    enum TokenType type;
    char *value;
    int line;
    int col;
} Token;

typedef struct {
    char* buffer;
    unsigned long buffer_len;
    unsigned long pos;
    unsigned long read_pos;
    char ch;
    int line;
    int col;
} Lexer;

const char *token_type_to_string(enum TokenType type);
void lexer_print_tokens(DynamicArray *tokens);
int lexer_tokenize(char *buffer, unsigned long length, DynamicArray *tokens);

#endif //LEXER_H
