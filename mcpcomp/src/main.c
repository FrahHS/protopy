#include <stdio.h>

#include "util.h"
#include "datatype.h"
#include "lexer.h"
#include "mparser.h"


int main(int argc, char *argv[]) {
    if(argc != 2) {
        printf("Error: not enough arguments!");
        return 1;
    }

    char *buffer;
    long buffer_len = read_source(argv[1], &buffer);

    // Lexical analysis
    DynamicArray tokens;
    dynamic_array_init(&tokens, sizeof(Token));
    lexer_tokenize(buffer, argv[1], buffer_len, &tokens);

    // Program parsing
    Program program = parser_parse(argv[1], &tokens);
    program_print(&program);

    return 0;
}
