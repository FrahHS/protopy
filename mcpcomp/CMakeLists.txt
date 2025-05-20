cmake_minimum_required(VERSION 3.10)
project(mcpcomp VERSION 0.1 LANGUAGES C)

set(CMAKE_C_STANDARD 99)

add_executable(mcpcomp
    src/main.c
    src/util.c
    src/datatype.c
    src/lexer.c
)

target_include_directories(mcpcomp PRIVATE include)
