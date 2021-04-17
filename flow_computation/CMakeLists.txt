cmake_minimum_required(VERSION 3.17)
project(flow_computation)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")

find_package( OpenCV REQUIRED )
set(SOURCE_FILES optical_flow.cpp)

add_executable(${PROJECT_NAME} optical_flow.cpp)

set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -lstdc++fs")

include_directories(${OpenCV_INCLUDE_DIRS})

target_link_libraries( ${PROJECT_NAME} ${OpenCV_LIBS} )