#ifndef MPARSER_H
#define MPARSER_H

#include "util.h"
#include "datatype.h"
#include "lexer.h"

typedef struct {
        const char *filename;
        DynamicArray *tokens;
        int protocol_version;
        unsigned int index;
} Parser;

typedef struct {
    DataType type;
    char *identifier;
    int size;
    int optional;
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

void parser_run(const char *filename, DynamicArray *tokens, Program *program);

#endif // MPARSER_H
