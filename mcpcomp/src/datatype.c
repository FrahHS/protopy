#include "datatype.h"

const DataType data_types[] = {
    DATATYPE(767, "BOOLEAN",                "Boolean",              "self.body += b\"\\x01\" if data else b\"\\x00\""   ),
    DATATYPE(767, "BYTE",                   "Byte",                 ""                                                  ),
    DATATYPE(767, "UNSIGNED_BYTE",          "UnsignedByte",         ""                                                  ),
    DATATYPE(767, "SHORT",                  "Short",                ""                                                  ),
    DATATYPE(767, "UNSIGNED_SHORT",         "UnsignedShort",        ""                                                  ),
    DATATYPE(767, "INT",                    "Int",                  ""                                                  ),
    DATATYPE(767, "LONG",                   "Long",                 ""                                                  ),
    DATATYPE(767, "FLOAT",                  "Float",                ""                                                  ),
    DATATYPE(767, "DOUBLE",                 "Double",               ""                                                  ),
    DATATYPE(767, "STRING",                 "String",               ""                                                  ),
    DATATYPE(767, "TEXT_COMPONENT",         "TextComponent",        ""                                                  ),
    DATATYPE(767, "JSON_TEXT_COMPONENT",    "JsonTextComponent",    ""                                                  ),
    DATATYPE(767, "IDENTIFIER",             "Identifier",           ""                                                  ),
    DATATYPE(767, "VARINT",                 "VarInt",               ""                                                  ),
    DATATYPE(767, "VARLONG",                "VarLong",              ""                                                  ),
    DATATYPE(767, "ENTITY_METADATA",        "EntityMetadata",       ""                                                  ),
    DATATYPE(767, "SLOT",                   "Slot",                 ""                                                  ),
    DATATYPE(767, "HASHED_SLOT",            "HashedSlot",           ""                                                  ),
    DATATYPE(767, "NBT",                    "NBT",                  ""                                                  ),
    DATATYPE(767, "POSITION",               "Position",             ""                                                  ),
    DATATYPE(767, "ANGLE",                  "Angle",                ""                                                  ),
    DATATYPE(767, "UUID",                   "UUID",                 ""                                                  ),
    DATATYPE(767, "BITSET",                 "BitSet",               ""                                                  ),
    DATATYPE(767, "FIXED_BITSET",           "FixedBitSet",          ""                                                  ),
    DATATYPE(767, "OPTIONAL_X",             "Optional",             ""                                                  ),
    DATATYPE(767, "PREFIXED_OPTIONAL_X",    "PrefixedOptional",     ""                                                  ),
    DATATYPE(767, "ARRAY_OF_X",             "Array",                ""                                                  ),
    DATATYPE(767, "PREFIXED_ARRAY_OF_X",    "PrefixedArray",        ""                                                  ),
    DATATYPE(767, "X_ENUM",                 "XEnum",                ""                                                  ),
    DATATYPE(767, "ENUM_SET",               "EnumSet",              ""                                                  ),
    DATATYPE(767, "BYTE_ARRAY",             "ByteArray",            ""                                                  ),
    DATATYPE(767, "ID_OR_X",                "IdOrX",                ""                                                  ),
    DATATYPE(767, "ID_SET",                 "IdSet",                ""                                                  ),
    DATATYPE(767, "SOUND_EVENT",            "SoundEvent",           ""                                                  ),
    DATATYPE(767, "CHAT_TYPE",              "ChatType",             ""                                                  ),
    DATATYPE(767, "TELEPORT_FLAGS",         "TeleportFlags",        ""                                                  ),
    DATATYPE(767, "RECIPE_DISPLAY",         "RecipeDisplay",        ""                                                  ),
    DATATYPE(767, "CHUNK_DATA",             "ChunkData",            ""                                                  ),
    DATATYPE(767, "LIGHT_DATA",             "LightData",            ""                                                  )
};


const int DATA_TYPE_SIZE = sizeof(data_types) / sizeof(data_types[0]);

const DataType *datatype_get_by_name(const char *type_name, int protocol) {
    for(int i = 0; i < DATA_TYPE_SIZE; i++) {
        if(strcmp(data_types[i].type_name, type_name) == 0 &&
            data_types[i].protocol == protocol) {
            return &data_types[i];
        }
    }
    return NULL;
}

int datatype_is_type_supported(const char *type_name, int protocol) {
    return datatype_get_by_name(type_name, protocol) != NULL;
}

void datatype_print_info(const DataType *type) {
    if(!type) {
        printf("DataType not found.\n");
        return;
    }
    printf("Type: %s\n", type->type_name);
    printf("Keyword: %s\n", type->keyword);
    printf("Protocol: %d\n", type->protocol);
    printf("Writer: %s\n", type->writer_implementation[0] ? type->writer_implementation : "(none)");
}

const DataType *datatype_get_by_keyword(const char *keyword, int protocol) {
    for(int i = 0; i < DATA_TYPE_SIZE; i++) {
        if(strcmp(data_types[i].keyword, keyword) == 0 &&
            data_types[i].protocol == protocol) {
            return &data_types[i];
        }
    }
    return NULL;
}

int datatype_is_keyword_supported_general(const char *keyword) {
    for(int i = 0; i < DATA_TYPE_SIZE; i++) {
        if(strcmp(data_types[i].keyword, keyword) == 0) {
            return 1;
        }
    }
    return 0;
}

int datatype_is_keyword_supported(const char *keyword, int protocol) {
    return datatype_get_by_keyword(keyword, protocol) != NULL;
}

const char *datatype_get_type_name_from_keyword(const char *keyword, int protocol) {
    const DataType *type = datatype_get_by_keyword(keyword, protocol);
    return type ? type->type_name : NULL;
}

const PacketState packet_states[] = {
    PACKETSTATE(767, "HANDSHAKING",   "HANDSHAKING"),
    PACKETSTATE(767, "STATUS",        "STATUS"),
    PACKETSTATE(767, "CONFIGURATION", "CONFIGURATION"),
    PACKETSTATE(767, "LOGIN",         "LOGIN"),
    PACKETSTATE(767, "PLAY",          "PLAY")
};

const int PACKET_STATE_COUNT = sizeof(packet_states) / sizeof(packet_states[0]);

const PacketState *packet_state_get_by_keyword(const char *keyword, int protocol) {
    for (int i = 0; i < PACKET_STATE_COUNT; i++) {
        if (strcmp(packet_states[i].keyword, keyword) == 0 &&
            packet_states[i].protocol == protocol) {
            return &packet_states[i];
        }
    }
    return NULL;
}

const PacketState *packet_state_get_by_keyword_general(const char *keyword) {
    for (int i = 0; i < PACKET_STATE_COUNT; i++) {
        if (strcmp(packet_states[i].keyword, keyword) == 0) {
            return &packet_states[i];
        }
    }
    return NULL;
}

int packet_state_is_supported(const char *keyword, int protocol) {
    return packet_state_get_by_keyword(keyword, protocol) != NULL;
}

void packet_state_print_all_for_protocol(int protocol) {
    printf("Packet states for protocol %d:\n", protocol);
    for (int i = 0; i < PACKET_STATE_COUNT; i++) {
        if (packet_states[i].protocol == protocol) {
            printf("  - %s (%s)\n", packet_states[i].keyword, packet_states[i].type_name);
        }
    }
}

int packet_state_is_supported_general(const char *keyword) {
    for(int i = 0; i < PACKET_STATE_COUNT; i++) {
        if(strcmp(packet_states[i].keyword, keyword) == 0) {
            return 1;
        }
    }
    return 0;
}

const char *packet_state_get_type_name(const char *keyword, int protocol) {
    const PacketState *state = packet_state_get_by_keyword(keyword, protocol);
    return state ? state->type_name : NULL;
}

const PacketBound packet_bound[] = {
    PACKETBOUND(767, "SERVER", "SERVER"),
    PACKETBOUND(767, "CLIENT", "CLIENT")
};

const int PACKET_BOUND_COUNT = sizeof(packet_bound) / sizeof(packet_bound[0]);

const PacketBound *packet_bound_get_by_keyword(const char *keyword, int protocol) {
    for (int i = 0; i < PACKET_BOUND_COUNT; i++) {
        if (strcmp(packet_bound[i].keyword, keyword) == 0 &&
            packet_bound[i].protocol == protocol) {
            return &packet_bound[i];
        }
    }
    return NULL;
}

const PacketBound *packet_bound_get_by_keyword_general(const char *keyword) {
    for (int i = 0; i < PACKET_BOUND_COUNT; i++) {
        if (strcmp(packet_bound[i].keyword, keyword) == 0) {
            return &packet_bound[i];
        }
    }
    return NULL;
}

int packet_bound_is_supported(const char *keyword, int protocol) {
    return packet_bound_get_by_keyword(keyword, protocol) != NULL;
}

int packet_bound_is_supported_general(const char *keyword) {
    for(int i = 0; i < PACKET_BOUND_COUNT; i++) {
        if(strcmp(packet_bound[i].keyword, keyword) == 0) {
            return 1;
        }
    }
    return 0;
}

void packet_bound_print_all_for_protocol(int protocol) {
    printf("Packet bounds for protocol %d:\n", protocol);
    for (int i = 0; i < PACKET_BOUND_COUNT; i++) {
        if (packet_bound[i].protocol == protocol) {
            printf("  - %s (%s)\n", packet_bound[i].keyword, packet_bound[i].type_name);
        }
    }
}

const char *packet_bound_get_type_name(const char *keyword, int protocol) {
    const PacketBound *bound = packet_bound_get_by_keyword(keyword, protocol);
    return bound ? bound->type_name : NULL;
}
