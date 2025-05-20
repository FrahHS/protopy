#include <string.h>
#include <stdlib.h>
#include "mparser.h"

void parser_show_expected(Parser *parser, TokenType expected, TokenType got) {
    printf( RED
        "%s(%d,%d): Syntax error: expected %s, got %s.\n" RESET,
        parser->filename,
        ((Token *)dynamic_array_get(parser->tokens, parser->index))->line,
        ((Token *)dynamic_array_get(parser->tokens, parser->index))->col,
        token_type_to_string(expected),
        token_type_to_string(got)
    );
}

PacketState str_to_packet_state(char *str) {
    if(strcmp(str, "HANDSHAKING")) {
        return HANDSHAKING;
    } else if (strcmp(str, "STATUS")) {
        return STATUS;
    } else if (strcmp(str, "CONFIGURATION")) {
        return CONFIGURATION;
    } else if (strcmp(str, "LOGIN")) {
        return LOGIN;
    } else if (strcmp(str, "PLAY")) {
        return PLAY;
    } else {
        printf("Invalid PacketState str: %s", str);
        return 1;
    }
}

char *packet_state_to_str(PacketState state) {
    if(state == HANDSHAKING) {
        return "HANDSHAKING";
    } else if(state == STATUS) {
        return "STATUS";
    } else if(state == CONFIGURATION) {
        return "CONFIGURATION";
    } else if(state == LOGIN) {
        return "LOGIN";
    } else if(state == PLAY) {
        return "PLAY";
    } else {
        printf("Invalid PacketState: %d", state);
        return 1;
    }
}

PacketBound str_to_packet_bound(char *str) {
    if(strcmp(str, "SERVER")) {
        return SERVER;
    } else if (strcmp(str, "CLIENT")) {
        return CLIENT;
    } else {
        printf("Invalid PacketBound str: %s", str);
        return 1;
    }
}

char *packet_bound_to_str(PacketBound bound) {
    if(bound == SERVER) {
        return "SERVER";
    } else if(bound == CLIENT) {
        return "CLIENT";
    } else {
        printf("Invalid PacketBound: %d", bound);
        return 1;
    }
}

void print_header(Header *header) {
    printf("Header:\n");
    printf("\tint protocol_version: %d\n", header->protocol_version);
    printf("\tpacket_id: %d\n", header->packet_id);
    printf("\tstate: %s\n", packet_state_to_str(header->state));
    printf("\tbound: %s\n", packet_bound_to_str(header->bound));
    printf("\n");
}
/*
void print_field_recursive(Field *field, int depth) {
    const char *indent = "    "; // 4 spazi per ogni livello
    for (int i = 0; i < depth; i++) printf("%s", indent);
    printf("Field %s:\n", field->identifier);

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("identifier: %s\n", field->identifier);

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("type: %s\n", token_type_to_string(field->type));

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("optional: %d\n", field->optional);

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("size: %d\n", field->size);

    // Ricorsione per Array
    if (field->type == ARRAY) {
        for (int i = 0; i < depth + 1; i++) printf("%s", indent);
        printf("sub_fields:\n");
        for (int i = 0; i < field->sub_fields->length; i++) {
            Field *sub = (Field *)dynamic_array_get(field->sub_fields, i);
            print_field_recursive(sub, depth + 2);
        }
    }
}


void print_packet(Packet *packet) {
    printf("Packet %s:\n", packet->identifier);
    for (int i = 0; i < packet->fields->length; i++) {
        Field *field = (Field *)dynamic_array_get(packet->fields, i);
        print_field_recursive(field, 1);
    }
    printf("\n");
}*/

void print(Program *program) {
    print_header(&program->header);
    //print_packet(&program->packet);
}

Token* parser_get_token_at(Parser* parser, unsigned long index) {
    return (Token*) dynamic_array_get(parser->tokens, index);
}

static int parser_current(Parser *parser, Token *token) {
    if(parser->index >= parser->tokens->length) {
        return 1;
    }

    Token *t = (Token *) dynamic_array_get(parser->tokens, parser->index);
    *token = *t;

    return 0;
}


static int parser_peek(Parser *parser, Token *token) {
    if(parser->index + 1 >= parser->tokens->length) {
        return 1;
    }

    token = dynamic_array_get(parser->tokens, parser->index + 1);

    return 0;
}

static int parser_advance(Parser *parser) {
    if(parser->index >= parser->tokens->length) {
        return 1;
    }

    parser->index++;

    return 0;
}

int header_assignment(Parser *parser, Header *header, char *identifier, TokenType expected_token) {
    Token token;

    parser_advance(parser);
    parser_current(parser, &token);
    if (token.type != ASSIGN) {
        parser_show_expected(parser, ASSIGN, token.type);
        return 1;
    }

    parser_advance(parser);
    parser_current(parser, &token);
    /*if(token.type != expected_token) {
        parser_show_expected(parser, expected_token, token.type);
        return 1;
    }*/

    if(strcmp(identifier, "protocol_version") == 0) {
        header->protocol_version = atoi(token.value);
    } else if (strcmp(identifier, "packet_id") == 0) {
        header->packet_id = (byte) strtol(token.value, NULL, 0);
    } else if (strcmp(identifier, "state") ==  0) {
        header->state = str_to_packet_state(token.value);
    } else if (strcmp(identifier, "bound") == 0) {
        header->bound = str_to_packet_bound(token.value);
    }

    parser_advance(parser);
    parser_current(parser, &token);
    if(token.type != SEMICOLON) {
        parser_show_expected(parser, SEMICOLON, token.type);
        return 1;
    }

    return 0;
}

int parser_build_header(Parser *parser, Header *header) {
    Token token;
    parser_current(parser, &token);

    if(token.value != "Header") {
        parser_show_expected(parser, HEADER, token.type);
        return 1;
    }
    parser_advance(parser);
    parser_current(parser, &token);

    if (token.value != "{") {
        parser_show_expected(parser, BRACKET_OPEN, token.type);
        return 1;
    }
    parser_advance(parser);
    parser_current(parser, &token);

    do {
        if(strcmp(token.value, "protocol_version") == 0) {
            header_assignment(parser, header, "protocol_version", LITERAL);
            parser->protocol_version = header->protocol_version;
            parser_advance(parser);
        } else if(strcmp(token.value, "packet_id") == 0) {
            header_assignment(parser, header, "packet_id", LITERAL);
            parser_advance(parser);
        } else if(strcmp(token.value, "state") == 0) {
            header_assignment(parser, header, "state", LITERAL);
            parser_advance(parser);
        } else if(strcmp(token.value, "bound") == 0) {
            header_assignment(parser, header, "bound", LITERAL);
            parser_advance(parser);
        } else {
            printf("Invalid Header identifier: %s", token.value);
            return 1;
        }
        parser_current(parser, &token);
    } while (token.value != "}");

    return 0;
}

/*
 * Edgecases: Optional(not mandatory), String(require a size), Array(different structure)
*/
/*int next_field(Parser *parser, Field *field) {
    Token token;

    field->optional = 0;
    field->size = 0;

    parser_current(parser, &token);

    // Optional case
    if(token.type == OPTIONAL) {
        field->optional = 1;
        parser_advance(parser);
        parser_current(parser, &token);
    }

    field->type = token.type;

    parser_advance(parser);
    parser_current(parser, &token);
    // String case
    if(field->type == STRING) {
        if (token.type != PARENTHESIS_OPEN) {
            parser_show_expected(parser, PARENTHESIS_OPEN, token.type);
            return 1;
        }

        parser_advance(parser);
        parser_current(parser, &token);
        if (token.type != INT_LITERAL) {
            parser_show_expected(parser, INT_LITERAL, token.type);
            return 1;
        }
        field->size = atoi(token.value);

        parser_advance(parser);
        parser_current(parser, &token);
        if (token.type != PARENTHESIS_CLOSE) {
            parser_show_expected(parser, PARENTHESIS_CLOSE, token.type);
            return 1;
        }
        parser_advance(parser);
        parser_current(parser, &token);
    }

    // Identifier
    if (token.type != STRING_LITERAL) {
        parser_show_expected(parser, STRING_LITERAL, token.type);
        return 1;
    }
    field->identifier = token.value;

    // Array case
    if(field->type == ARRAY) {
        parser_advance(parser);
        parser_current(parser, &token);
        if (token.type != BRACKET_OPEN) {
            parser_show_expected(parser, BRACKET_OPEN, token.type);
            return 1;
        }
        parser_advance(parser);
        parser_current(parser, &token);

        do {
            Field *sub_field = malloc(sizeof(Field));
            sub_field->sub_fields = malloc(sizeof(DynamicArray));
            dynamic_array_init(sub_field->sub_fields, sizeof(Field));

            next_field(parser, sub_field);
            parser_current(parser, &token);
            dynamic_array_append(field->sub_fields, sub_field);

            free(sub_field);
        } while (token.type != BRACKET_CLOSE);
    }

    // Semicolumn
    parser_advance(parser);
    parser_current(parser, &token);
    if(token.type != SEMICOLON) {
        parser_show_expected(parser, SEMICOLON, token.type);
        return 1;
    }
    parser_advance(parser);

    return 0;
}*/

/*int packet_assignment(Parser *parser, Packet *packet) {
    Token token;

    do {
        // Init field and subfields
        Field *field = malloc(sizeof(Field));
        field->sub_fields = malloc(sizeof(DynamicArray));
        dynamic_array_init(field->sub_fields, sizeof(Field));

        next_field(parser, field);
        parser_current(parser, &token);
        dynamic_array_append(packet->fields, field);

        free(field);
    } while (token.type != BRACKET_CLOSE);

    return 0;
}*/

/*int build_packet(Parser *parser, Packet *packet) {
    Token token;

    packet->fields = malloc(sizeof(DynamicArray));
    dynamic_array_init(packet->fields, sizeof(Field));

    parser_current(parser, &token);

    if(token.type != PACKET) {
        parser_show_expected(parser, PACKET, token.type);
        return 1;
    }
    parser_advance(parser);
    parser_current(parser, &token);

    if (token.type != STRING_LITERAL) {
        parser_show_expected(parser, STRING_LITERAL, token.type);
        return 1;
    }
    packet->identifier = token.value;
    parser_advance(parser);
    parser_current(parser, &token);

    if (token.type != BRACKET_OPEN) {
        parser_show_expected(parser, BRACKET_OPEN, token.type);
        return 1;
    }
    parser_advance(parser);
    parser_current(parser, &token);

    // Fields assignment
    do {
        packet_assignment(parser, packet);
        parser_current(parser, &token);
    } while (token.type != BRACKET_CLOSE);

    return 0;
}*/

int parser_build_program(Parser* parser, Program *program) {
    Token token;
    Header *header = &(program->header);
    Packet *packet = &(program->packet);

    parser_build_header(parser, header);
    parser_current(parser, &token);
    if (token.type != BRACKET_CLOSE) {
        return 1;
    }
    parser_advance(parser);

    /*build_packet(parser, packet);
    parser_current(parser, &token);
    if (token.type != BRACKET_CLOSE) {
        return 1;
    }

    parser_advance(parser);*/
    parser_current(parser, &token);
    if (token.type != END) {
        return 1;
    }

    return 0;
}

void parser_run(const char *filename, DynamicArray *tokens, Program *program) {
    Parser parser = {
        .filename = filename,
        .tokens = tokens,
        .index = 0,
    };

    if(!parser_build_program(&parser, program)) {
        printf("Parsing stage completed with success!\n");
    } else {
        printf("Parsing exited with errors!\n");
    }
}
