#ifndef LEXER_H
#define LEXER_H

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#include "util.h"
#include "datatype.h"

typedef enum {
    // Single-character tokens.
    PARENTHESIS_OPEN, PARENTHESIS_CLOSE, BRACKET_OPEN, BRACKET_CLOSE,
    SEMICOLON, EQUAL,

    // One or two character tokens.
    LINE_COMMENT,

    // Literals.
    IDENTIFIER, DATATYPE, PACKETSTATE, PACKETBOUND, STRING_LITERAL, INT_LITERAL, DOUBLE_LITERAL, BYTE_LITERAL,

    // Keywords.
    HEADER, PACKET, FALSE, TRUE,

    // Special tokens.
    END, UNKNOWN
} TokenType;

typedef struct {
    enum TokenType type;
    char *literal;
    int line;
    int col;
} Token;

typedef struct {
    char* filename;
    char* buffer;
    unsigned long buffer_len;
    unsigned long pos;
    unsigned long read_pos;
    char ch;
    int line;
    int col;
} Lexer;

const char *token_type_to_string(enum TokenType type);
void token_print(Token tokens);
int lexer_tokenize(char *buffer, char *filename, unsigned long length, DynamicArray *tokens);

#endif //LEXER_H
