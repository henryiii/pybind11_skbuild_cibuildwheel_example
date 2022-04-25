cmake_minimum_required(VERSION 3.14...3.22)

project(cli11 VERSION "0.1")

include(GNUInstallDirs)
include(FetchContent)

FetchContent_Declare(
  pybind11
  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.9.2.tar.gz
  URL_HASH
    SHA256=6bd528c4dbe2276635dc787b6b1f2e5316cf6b49ee3e150264e455a0d68d19c1)
FetchContent_MakeAvailable(pybind11)

FetchContent_Declare(
  cli11
  URL https://github.com/CLIUtils/CLI11/archive/refs/tags/v2.2.0.tar.gz
  URL_HASH
    SHA256=d60440dc4d43255f872d174e416705f56ba40589f6eb07727f76376fb8378fd6)
FetchContent_MakeAvailable(cli11)

pybind11_add_module(cli11 MODULE src/cli11.cpp)

target_link_libraries(cli11 PRIVATE CLI11::CLI11)
target_compile_features(cli11 PUBLIC cxx_std_14)

install(TARGETS cli11 DESTINATION .)
