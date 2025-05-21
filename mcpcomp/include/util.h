#ifndef UTIL_H
#define UTIL_H

#include <stdio.h>
#include <stdlib.h>

#define MAX_STR_LEN 4096

#define RESET   "\033[0m"
#define BLACK   "\033[30m"      /* Black */
#define RED     "\033[31m"      /* Red */
#define GREEN   "\033[32m"      /* Green */
#define YELLOW  "\033[33m"      /* Yellow */
#define BLUE    "\033[34m"      /* Blue */
#define MAGENTA "\033[35m"      /* Magenta */
#define CYAN    "\033[36m"      /* Cyan */
#define WHITE   "\033[37m"      /* White */
#define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
#define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
#define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
#define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
#define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */

typedef unsigned char byte;

typedef struct {
    void *items;
    unsigned long item_size;
    unsigned long length;
} DynamicArray;

void dynamic_array_init(DynamicArray *dynamic_array, unsigned long item_size);
void dynamic_array_append(DynamicArray *dynamic_array, const void *item);
void *dynamic_array_get(DynamicArray *dynamic_array, unsigned long index);
int append_char(char *str, char c);
long read_source(const char *filename, char **buffer);

#endif // UTIL_H
