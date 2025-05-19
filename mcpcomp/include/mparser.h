#ifndef MPARSER_H
#define MPARSER_H

#include "util.h"
#include "lexer.h"

typedef struct {
        const char *filename;
        DynamicArray *tokens;
        unsigned int index;
} Parser;

typedef enum {
    HANDSHAKING,
    STATUS,
    CONFIGURATION,
    LOGIN,
    PLAY,
} PacketState;

typedef enum {
    SERVER,
    CLIENT
} PacketBound;

typedef struct {
    TokenType type;
    int size;
    int optional;
    char *identifier;
    DynamicArray *sub_fields;
} Field;

typedef struct {
    int protocol_version;
    byte packet_id;
    PacketState state;
    PacketBound bound;
} Header;

typedef struct {
    char *identifier;
    DynamicArray *fields;
} Packet;

typedef struct {
    Header header;
    Packet packet;
} Program;

void parser_show_expected(Parser *parser, TokenType expected, TokenType got) {
    printf(
        "%s(%d,%d): Syntax error: expected %s, got %s.\n",
        parser->filename,
        ((Token *)dynamic_array_get(parser->tokens, parser->index))->line,
        ((Token *)dynamic_array_get(parser->tokens, parser->index))->col,
        token_type_to_string(expected),
        token_type_to_string(got)
    );
}

void parser_run(const char *filename, DynamicArray *tokens, Program *program);

#endif // MPARSER_H
