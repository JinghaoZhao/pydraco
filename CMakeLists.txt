cmake_minimum_required(VERSION 3.18)
project(pydraco)

add_subdirectory(pybind11)
add_subdirectory(draco)
pybind11_add_module(pydraco src/main.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(pydraco PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
target_link_libraries(pydraco PRIVATE libdraco.a)
