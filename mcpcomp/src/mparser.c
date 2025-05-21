#include "mparser.h"

void parser_print_error(Parser *p, char *message, ...) {
    printf(
        RED "%s(%d,%d): %s\n" RESET,
        p->filename,
        p->token->line,
        p->token->col,
        message
    );
}

void parser_print_expected(Parser *p, TokenType expected, Token *got) {
    char msg[256];
    snprintf(
        msg, sizeof(msg), "Syntax error: %s expected, got %s.",
        token_type_to_string(expected),
        got ? got->literal : "(null)"
    );

    parser_print_error(p, msg);
}

int parser_expect(Parser *p, TokenType expected) {
    if(p->token->type != expected) {
        parser_print_expected(p, expected, p->token);
        return 0;
    }

    return 1;
}


void parser_panic(Parser *p, char *message) {
    parser_print_error(p, message);
    exit(EXIT_FAILURE);
}

void header_print(Header *header) {
    printf("Header:\n");
    printf("\tint protocol_version: %d\n", header->protocol_version);
    printf("\tpacket_id: %d\n", header->packet_id);
    printf("\tstate: %s\n", header->state.keyword);
    printf("\tbound: %s\n", header->bound.keyword);
    printf("\n");
}

void field_print(Field *field, int depth) {
    const char *indent = "    "; // 4 spazi per ogni livello
    for (int i = 0; i < depth; i++) printf("%s", indent);
    printf("Field %s:\n", field->identifier);

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("identifier: %s\n", field->identifier);

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("type: %s\n", field->type.type_name);

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("optional: %d\n", field->optional);

    for (int i = 0; i < depth + 1; i++) printf("%s", indent);
    printf("size: %d\n", field->size);

    // Array recursion
    if (field->type.type_name == "ARRAY_OF_X") {
        for (int i = 0; i < depth + 1; i++) printf("%s", indent);
        printf("sub_fields:\n");
        for (unsigned long i = 0; i < field->sub_fields.length; i++) {
            Field *sub = (Field *)dynamic_array_get(&field->sub_fields, i);
            field_print(sub, depth + 2);
        }
    }
}


void packet_print(Packet *packet) {
    printf("Packet %s:\n", packet->identifier);
    for (unsigned long i = 0; i < packet->fields.length; i++) {
        Field *field = (Field *)dynamic_array_get(&packet->fields, i);
        field_print(field, 1);
    }
    printf("\n");
}

void program_print(Program *program) {
    header_print(&program->header);
    packet_print(&program->packet);
}

void program_init(Program *program){
    dynamic_array_init(&program->packet.fields, sizeof(Field));
}

Token *parser_peek(Parser *p) {
    if(p->index + 1 >= p->tokens->length) {
        return NULL;
    }

    return dynamic_array_get(p->tokens, p->index + 1);
}

Token *parser_next(Parser *p) {
    if(p->index + 1 >= p->tokens->length) {
        return NULL;
    }

    p->index++;
    p->token = dynamic_array_get(p->tokens, p->index);

    return p->token;
}

void parser_init(Parser *p, char *filename, DynamicArray *tokens) {
    p->filename = filename;
    p->index = 0;
    p->tokens = tokens;
    p->token = dynamic_array_get(p->tokens, p->index);
}

int parser_parse_header_parameter(Parser *p, Header *header) {
    // Identifier
    parser_expect(p, IDENTIFIER);
    char *identifier = p->token->literal;
    parser_next(p);

    // Assignment operator
    parser_expect(p, EQUAL);
    parser_next(p);

    // Literal value to assignment
    if(strcmp(identifier, "protocol_version") == 0) {
        parser_expect(p, INT_LITERAL);
        header->protocol_version = atoi(p->token->literal);
    } else if(strcmp(identifier, "packet_id") == 0) {
        parser_expect(p, BYTE_LITERAL);
        header->packet_id = (byte) strtol(p->token->literal, NULL, 0);
    } else if(strcmp(identifier, "state") == 0) {
        parser_expect(p, PACKETSTATE);
        header->state = *packet_state_get_by_keyword_general(p->token->literal);
    } else if(strcmp(identifier, "bound") == 0) {
        parser_expect(p, PACKETBOUND);
        header->bound = *packet_bound_get_by_keyword_general(p->token->literal);
    }
    parser_next(p);

    // Semicolon to end the assignment operation
    parser_expect(p, SEMICOLON);
    parser_next(p);

    return 0;
}

int parser_parse_header(Parser *p, Header *header) {
    parser_expect(p, HEADER);
    parser_next(p);

    parser_expect(p, BRACKET_OPEN);
    parser_next(p);

    while(p->token->type != BRACKET_CLOSE) {
        parser_parse_header_parameter(p, header);
    };

    parser_next(p);

    return 0;
}

Field *parser_parse_packet_field(Parser *p, Packet *packet) {
    Field *field = malloc(sizeof(Field));
    memset(field, 0, sizeof(Field));

    // Identifier
    parser_expect(p, DATATYPE);
    field->type = *datatype_get_by_keyword(p->token->literal, p->protocol_version);
    parser_next(p);

    if(strcmp(field->type.type_name, "OPTIONAL_X") == 0) {
        field->optional = 1;
        parser_expect(p, DATATYPE);
        field->type = *datatype_get_by_keyword(p->token->literal, p->protocol_version);
        parser_next(p);
    }

    if(strcmp(field->type.type_name, "STRING") == 0) {
        parser_expect(p, PARENTHESIS_OPEN);
        parser_next(p);

        parser_expect(p, INT_LITERAL);
        field->size = atoi(p->token->literal);
        parser_next(p);

        parser_expect(p, PARENTHESIS_CLOSE);
        parser_next(p);
    }

    parser_expect(p, IDENTIFIER);
    field->identifier  = p->token->literal;
    parser_next(p);

    if(strcmp(field->type.type_name, "ARRAY_OF_X") == 0) {
        dynamic_array_init(&field->sub_fields, sizeof(Field));
        parser_expect(p, BRACKET_OPEN);
        parser_next(p);

        while(p->token->type != BRACKET_CLOSE) {
            Field *sub_field = parser_parse_packet_field(p, packet);
            dynamic_array_append(&field->sub_fields, sub_field);
            free(sub_field);
        };

        parser_next(p);
    }

    // Semicolon to end the assignment operation
    parser_expect(p, SEMICOLON);
    parser_next(p);

    return field;
}

int parser_parse_packet(Parser *p, Packet *packet) {
    parser_expect(p, PACKET);
    parser_next(p);

    parser_expect(p, IDENTIFIER);
    packet->identifier = p->token->literal;
    parser_next(p);

    parser_expect(p, BRACKET_OPEN);
    parser_next(p);

    while(p->token->type != BRACKET_CLOSE) {
        Field *field = parser_parse_packet_field(p, packet);
        dynamic_array_append(&packet->fields, field);
        free(field);
    };

    parser_next(p);

    return 0;
}

Program parser_parse(char *filename, DynamicArray *tokens) {
    Program program;
    program_init(&program);

    Parser parser;
    parser_init(&parser, filename, tokens);

    // Header
    parser_parse_header(&parser, &program.header);
    parser.protocol_version = program.header.protocol_version;

    // Packet
    dynamic_array_init(&program.packet.fields, sizeof(Field));
    parser_parse_packet(&parser, &program.packet);

    return program;
}
