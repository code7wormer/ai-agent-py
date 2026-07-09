import os

def write_file(working_directory:str,file_path:str,content:str)->str:
    try:
        abs_working_directory=os.path.abspath(working_directory)
        abs_file_path=os.path.normpath(os.path.join(abs_working_directory,file_path))
        is_valid=os.path.commonpath([abs_file_path,abs_working_directory])==abs_working_directory
        if is_valid:
            if os.path.isdir(abs_file_path):
                return f'Error: Cannot write to "{file_path}" as it is a directory'
            else:
                os.makedirs(os.path.dirname(abs_file_path),exist_ok=True)
                with open(abs_file_path,"w") as f:
                    f.write(content)
                    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        else:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: {e}'