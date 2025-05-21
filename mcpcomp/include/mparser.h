#ifndef MPARSER_H
#define MPARSER_H

#include "util.h"
#include "datatype.h"
#include "lexer.h"

typedef struct {
        const char *filename;
        DynamicArray *tokens;
        Token *token;
        int protocol_version;
        unsigned int index;
} Parser;

typedef struct {
    DataType type;
    char *identifier;
    int size;
    int optional;
    DynamicArray sub_fields;
} Field;

typedef struct {
    int protocol_version;
    byte packet_id;
    PacketState state;
    PacketBound bound;
} Header;

typedef struct {
    char *identifier;
    DynamicArray fields;
} Packet;

typedef struct {
    Header header;
    Packet packet;
} Program;

Program parser_parse(char *filename, DynamicArray *tokens);
void program_print(Program *program);

#endif // MPARSER_H
