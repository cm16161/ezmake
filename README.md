# EZMake

This script is designed to quickly setup a CMake project with the following structure:
```
.
├── CMakeLists.txt
├── build
├── inc
│   └── test.hpp
└── src
    └── main.cpp
```
So that a user can start developing right away.
The goal is to remove the barrier to entry for getting started with CMake for those unfamiliar with it.

# Install

Run:
```bash
install.sh
```

This places the ezmake script and templates into a newly created /opt/ezmake diretory
Additionally it creates a symlink in /usr/local/bin/ezmake -> /opt/ezmake/ezmake

# Uninstall
Run:
```bash
uninstall.sh
```

This removes the /opt/ezmake directory and /usr/local/bin/ezmake link
