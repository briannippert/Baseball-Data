# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Users/briannippert/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/182.4505.18/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/briannippert/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/182.4505.18/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/briannippert/Documents/GitHub/Baseball-Data/CPP

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/CPP.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/CPP.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/CPP.dir/flags.make

CMakeFiles/CPP.dir/main.cpp.o: CMakeFiles/CPP.dir/flags.make
CMakeFiles/CPP.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/briannippert/Documents/GitHub/Baseball-Data/CPP/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/CPP.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CPP.dir/main.cpp.o -c /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/main.cpp

CMakeFiles/CPP.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CPP.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/main.cpp > CMakeFiles/CPP.dir/main.cpp.i

CMakeFiles/CPP.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CPP.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/main.cpp -o CMakeFiles/CPP.dir/main.cpp.s

# Object files for target CPP
CPP_OBJECTS = \
"CMakeFiles/CPP.dir/main.cpp.o"

# External object files for target CPP
CPP_EXTERNAL_OBJECTS =

CPP: CMakeFiles/CPP.dir/main.cpp.o
CPP: CMakeFiles/CPP.dir/build.make
CPP: CMakeFiles/CPP.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/briannippert/Documents/GitHub/Baseball-Data/CPP/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable CPP"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CPP.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/CPP.dir/build: CPP

.PHONY : CMakeFiles/CPP.dir/build

CMakeFiles/CPP.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/CPP.dir/cmake_clean.cmake
.PHONY : CMakeFiles/CPP.dir/clean

CMakeFiles/CPP.dir/depend:
	cd /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/briannippert/Documents/GitHub/Baseball-Data/CPP /Users/briannippert/Documents/GitHub/Baseball-Data/CPP /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/cmake-build-debug /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/cmake-build-debug /Users/briannippert/Documents/GitHub/Baseball-Data/CPP/cmake-build-debug/CMakeFiles/CPP.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/CPP.dir/depend

