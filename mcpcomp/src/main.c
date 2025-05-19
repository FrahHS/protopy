#include <stdio.h>

#include "util.h"
#include "lexer.c"
#include "parser.c"

int main(int argc, char *argv[]) {
    if(argc != 2) {
        printf("Error: not enough arguments!");
        return 1;
    }

    char *buffer;
    long buffer_len = read_source(argv[1], &buffer);

    DynamicArray tokens;
    dynamic_array_init(&tokens, sizeof(Token));

    lexer_tokenize(buffer, buffer_len, &tokens);

    Program program;
    parser_run(argv[1], &tokens, &program);
    print(&program);

    return 0;
}
