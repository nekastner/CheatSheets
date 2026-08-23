cmake_minimum_required(VERSION 4.3)
project(cmocka C)

set(CMAKE_C_STANDARD 99)

find_package(cmocka REQUIRED)

add_library(calculator_lib
        src/calculator.c)
target_include_directories(calculator_lib PUBLIC src)

add_executable(cmocka main.c)
target_link_libraries(cmocka PRIVATE calculator_lib)

add_executable(cmocka_test tests/main_test.c)
target_link_libraries(cmocka_test PRIVATE calculator_lib cmocka::cmocka)

enable_testing()
add_test(NAME Testing COMMAND cmocka_test)