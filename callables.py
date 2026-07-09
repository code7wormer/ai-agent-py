schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads and returns the contents of a specified file relative to the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file, relative to the working directory.",
                },
            },
            "required": ["file_path"],
        },
    },
}
schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file in the working directory with optional command-line arguments.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file, relative to the working directory.",
                },
                "args": {
                    "type": "array",
                    "description": "Optional command-line arguments to pass to the Python program.",
                    "items": {
                        "type": "string",
                    },
                },
            },
            "required": ["file_path"],
        },
    },
}
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text to a file relative to the working directory, creating parent directories if necessary.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file, relative to the working directory.",
                },
                "content": {
                    "type": "string",
                    "description": "The text to write to the file.",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
available_functions = [
    schema_get_files_info,schema_write_file,schema_get_file_content,schema_write_file
]