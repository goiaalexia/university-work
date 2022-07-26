# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\seminar_6_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\seminar_6_autogen.dir\\ParseCache.txt"
  "seminar_6_autogen"
  )
endif()
