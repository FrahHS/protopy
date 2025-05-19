#ifndef UTIL_H
#define UTIL_H

#include <stdio.h>
#include <stdlib.h>

#define MAX_STR_LEN 4096

typedef unsigned char byte;

typedef struct {
    void *items;
    unsigned long item_size;
    unsigned long length;
} DynamicArray;

void dynamic_array_init(DynamicArray *dynamic_array, unsigned long item_size) {
    dynamic_array->items = NULL;
    dynamic_array->item_size = item_size;
    dynamic_array->length = 0;
}

void dynamic_array_append(DynamicArray *dynamic_array, const void *item) {
    void *new_items;

    new_items = realloc(dynamic_array->items, (dynamic_array->length + 1) * dynamic_array->item_size);

    dynamic_array->items = new_items;

    // Copy item into the newly allocated position
    memcpy((char *)dynamic_array->items + dynamic_array->length * dynamic_array->item_size, item, dynamic_array->item_size);

    dynamic_array->length++;
}

void *dynamic_array_get(DynamicArray *dynamic_array, unsigned long index) {
    if(index >= dynamic_array->length) {
        return NULL;
    }

    return (char *)dynamic_array->items + index * dynamic_array->item_size;
}

void append_char(char *str, char c) {
    size_t len = strlen(str);
    if(len == MAX_STR_LEN - 1) {
        printf("Error: Keyword exceded max length of %d", MAX_STR_LEN);
        return 1;
    }

    str[len] = c;
    str[len + 1] = '\0';
}

long read_source(const char *filename, char **buffer) {
    if (filename == NULL || buffer == NULL) {
        printf("Invalid source file name.\n");
        return -1;
    }

    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Failed to open the file: %s\n", filename);
        return -1;
    }

    fseek(file, 0, SEEK_END);
    long fsize = ftell(file);
    rewind(file);

    *buffer = (char*) malloc(fsize + 1);
    if (*buffer == NULL) {
        printf("Memory allocation failed.\n");
        fclose(file);
        return -1;
    }

    size_t read = fread(*buffer, 1, fsize, file);
    if (read != fsize) {
        printf("Failed to read the entire file.\n");
        free(*buffer);
        fclose(file);
        return -1;
    }

    (*buffer)[fsize] = '\0';
    fclose(file);

    return fsize;
}

#endif // UTIL_H
