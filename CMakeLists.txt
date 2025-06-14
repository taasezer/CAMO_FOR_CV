cmake_minimum_required(VERSION 3.20)
project(CAMO_CM_CPP)

# C++17 standardını kullan
set(CMAKE_CXX_STANDARD 17)

# OpenCV'yi bul
find_package(OpenCV REQUIRED)

# Çalıştırılabilir dosya oluştur
add_executable(CAMO_CM_CPP main.cpp)

# OpenCV kütüphanelerini bağla
target_link_libraries(CAMO_CM_CPP ${OpenCV_LIBS})