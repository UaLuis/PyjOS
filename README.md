# PyjOS

Псевдо-ОС на Python3.13 (Pseudo-OS on Python3.13)

## About

PyjOS is a simple pseudo-operating system implementation written in Python 3.13 that provides a command-line interface with basic file operations and system commands.

## Features

- Interactive command-line interface
- Basic file operations
- System information display
- Text manipulation capabilities

## Commands

- `help` - Display available commands
- `neo` - Show system information (similar to neofetch)
- `spawn` - Create a new file with three lines of text
- `burn` - Delete a file
- `say` - Display file contents
- `print` - Print text to console
- `quit` - Exit the system

## System Requirements

- Python 3.13
- No additional dependencies required

## Usage

To start PyjOS, run:

```bash
python main.py
```

After starting, you'll see the prompt:
```
(pyjos) \
```

## File Structure

- `main.py` - Entry point of the system
- `console_pyjos.py` - Console implementation and command handling
- `storage_pyjos.py` - File storage and management functionality

## Implementation Details

PyjOS implements a simple in-memory file system where:
- Files can contain three lines of text
- File operations are performed in memory
- The system provides a basic command set for file manipulation

## Author

Created by Luis (@UaLuis)

## Version

Current Version: 0.1