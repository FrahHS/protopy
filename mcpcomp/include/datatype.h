#ifndef DATATYPE_H
#define DATATYPE_H

#include <stdio.h>

typedef struct {
    const char *type_name;
    const char *keyword;
    int protocol;
    const char *writer_implementation;
} DataType;

typedef struct {
    const char *type_name;
    const char *keyword;
    int protocol;
} PacketState;

typedef struct {
    const char *type_name;
    const char *keyword;
    int protocol;
} PacketBound;

extern const DataType data_types[];
extern const int DATA_TYPE_COUNT;

const DataType *datatype_get_by_name(const char *type_name, int protocol);
int datatype_is_type_supported(const char *type_name, int protocol);
void datatype_print_info(const DataType *type);

const DataType *datatype_get_by_keyword(const char *keyword, int protocol);
int datatype_is_keyword_supported_general(const char *keyword);
int datatype_is_keyword_supported(const char *keyword, int protocol);
const char *datatype_get_type_name_from_keyword(const char *keyword, int protocol);

const PacketState *packet_state_get_by_keyword(const char *keyword, int protocol);
const PacketState *packet_state_get_by_keyword_general(const char *keyword);
int packet_state_is_supported_general(const char *keyword);
int packet_state_is_supported(const char *keyword, int protocol);
void packet_state_print_all_for_protocol(int protocol);
const char *packet_state_get_type_name(const char *keyword, int protocol);

const PacketBound *packet_bound_get_by_keyword(const char *keyword, int protocol);
const PacketBound *packet_bound_get_by_keyword_general(const char *keyword);
int packet_bound_is_supported_general(const char *keyword);
int packet_bound_is_supported(const char *keyword, int protocol);
void packet_bound_print_all_for_protocol(int protocol);
const char *packet_bound_get_type_name(const char *keyword, int protocol);

#endif // DATATYPE_H
