#include <stdio.h>

#include "util.h"
#include "datatype.h"
#include "lexer.h"


int main(int argc, char *argv[]) {
    if(argc != 2) {
        printf("Error: not enough arguments!");
        return 1;
    }

    char *buffer;
    long buffer_len = read_source(argv[1], &buffer);

    DynamicArray tokens;
    dynamic_array_init(&tokens, sizeof(Token));

    lexer_tokenize(buffer, argv[1], buffer_len, &tokens);

    for(unsigned long i = 0; i < tokens.length; i++)
        token_print(*(Token *)dynamic_array_get(&tokens, i));
/*
    Program program;
    parser_run(argv[1], &tokens, &program);
    print(&program);

    datatype_print_info(datatype_get_by_name("BOOLEAN", 767));*/

    return 0;
}
