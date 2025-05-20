#include "datatype.h"

const DataType data_types[] = {
    /* PROTOCOL VERSION 767 */

    // DataType: Boolean
    {
        .type_name = "BOOLEAN",
        .keyword = "Boolean",
        .protocol = 767,
        .writer_implementation = "self.body += b\"\\x01\" ifdata else b\"\\x00\""
    },

    // DataType: Byte
    {
        .type_name = "BYTE",
        .keyword = "Byte",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Unsigned Byte
    {
        .type_name = "UNSIGNED_BYTE",
        .keyword = "UnsignedByte",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Short
    {
        .type_name = "SHORT",
        .keyword = "Short",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Unsigned Short
    {
        .type_name = "UNSIGNED_SHORT",
        .keyword = "UnsignedShort",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Int
    {
        .type_name = "INT",
        .keyword = "Int",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Long
    {
        .type_name = "LONG",
        .keyword = "Long",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Float
    {
        .type_name = "FLOAT",
        .keyword = "Float",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Double
    {
        .type_name = "DOUBLE",
        .keyword = "Double",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: String
    {
        .type_name = "STRING",
        .keyword = "String",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: TextComponent
    {
        .type_name = "TEXT_COMPONENT",
        .keyword = "TextComponent",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: JsonTextComponent
    {
        .type_name = "JSON_TEXT_COMPONENT",
        .keyword = "JsonTextComponent",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Identifier
    {
        .type_name = "IDENTIFIER",
        .keyword = "Identifier",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: VarInt
    {
        .type_name = "VARINT",
        .keyword = "VarInt",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: VarLong
    {
        .type_name = "VARLONG",
        .keyword = "VarLong",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: EntityMetadata
    {
        .type_name = "ENTITY_METADATA",
        .keyword = "EntityMetadata",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Slot
    {
        .type_name = "SLOT",
        .keyword = "Slot",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: HashedSlot
    {
        .type_name = "HASHED_SLOT",
        .keyword = "HashedSlot",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: NBT
    {
        .type_name = "NBT",
        .keyword = "NBT",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Position
    {
        .type_name = "POSITION",
        .keyword = "Position",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Angle
    {
        .type_name = "ANGLE",
        .keyword = "Angle",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: UUID
    {
        .type_name = "UUID",
        .keyword = "UUID",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: BitSet
    {
        .type_name = "BITSET",
        .keyword = "BitSet",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: FixedBitSet
    {
        .type_name = "FIXED_BITSET",
        .keyword = "FixedBitSet",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Optional<X>
    {
        .type_name = "OPTIONAL_X",
        .keyword = "Optional",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: PrefixedOptional<X>
    {
        .type_name = "PREFIXED_OPTIONAL_X",
        .keyword = "PrefixedOptional",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: Array<X>
    {
        .type_name = "ARRAY_OF_X",
        .keyword = "Array",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: PrefixedArray<X>
    {
        .type_name = "PREFIXED_ARRAY_OF_X",
        .keyword = "PrefixedArray",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: X_ENUM
    {
        .type_name = "X_ENUM",
        .keyword = "XEnum",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: EnumSet
    {
        .type_name = "ENUM_SET",
        .keyword = "EnumSet",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: ByteArray
    {
        .type_name = "BYTE_ARRAY",
        .keyword = "ByteArray",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: IdOrX
    {
        .type_name = "ID_OR_X",
        .keyword = "IdOrX",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: IdSet
    {
        .type_name = "ID_SET",
        .keyword = "IdSet",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: SoundEvent
    {
        .type_name = "SOUND_EVENT",
        .keyword = "SoundEvent",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: ChatType
    {
        .type_name = "CHAT_TYPE",
        .keyword = "ChatType",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: TeleportFlags
    {
        .type_name = "TELEPORT_FLAGS",
        .keyword = "TeleportFlags",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: RecipeDisplay
    {
        .type_name = "RECIPE_DISPLAY",
        .keyword = "RecipeDisplay",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: ChunkData
    {
        .type_name = "CHUNK_DATA",
        .keyword = "ChunkData",
        .protocol = 767,
        .writer_implementation = ""
    },

    // DataType: LightData
    {
        .type_name = "LIGHT_DATA",
        .keyword = "LightData",
        .protocol = 767,
        .writer_implementation = ""
    }
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
    /* PROTOCOL VERSION 767 */

    // PacketState: HANDSHAKING
    {
        .type_name = "HANDSHAKING",
        .keyword = "HANDSHAKING",
        .protocol = 767,
    },

    // PacketState: STATUS
    {
        .type_name = "STATUS",
        .keyword = "STATUS",
        .protocol = 767,
    },

    // PacketState: CONFIGURATION
    {
        .type_name = "CONFIGURATION",
        .keyword = "CONFIGURATION",
        .protocol = 767,
    },

    // PacketState: LOGIN
    {
        .type_name = "LOGIN",
        .keyword = "LOGIN",
        .protocol = 767,
    },

    // PacketState: PLAY
    {
        .type_name = "PLAY",
        .keyword = "PLAY",
        .protocol = 767,
    }
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
    /* PROTOCOL VERSION 767 */

    // PacketBound: SERVER
    {
        .type_name = "SERVER",
        .keyword = "SERVER",
        .protocol = 767,
    },

    // PacketBound: CLIENT
    {
        .type_name = "CLIENT",
        .keyword = "CLIENT",
        .protocol = 767,
    }
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
