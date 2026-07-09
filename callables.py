from collections.abc import Callable
import json

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
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
        "name": "run_python",
        "description": "Runs a Python file. Use this when the user asks to execute, run, test, or launch a Python script.",
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
    schema_get_files_info,schema_write_file,schema_get_file_content,schema_run_python_file
]

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map: dict[str, Callable[..., str]] = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python": run_python_file,
    }
    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }
    function_args["working_directory"] = "./calculator"

    result = function_map[function_name](**function_args)

    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }