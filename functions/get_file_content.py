import os


def get_file_content(working_directory:str, file_path:str) ->str:
    try:
        abs_working_directory=os.path.abspath(working_directory)
        abs_file_path=os.path.normpath(os.path.join(abs_working_directory,file_path))
        is_valid=os.path.commonpath([abs_file_path,abs_working_directory])==abs_working_directory
        if is_valid:
            if not os.path.isfile(abs_file_path):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            else:
                with open(abs_file_path,"r") as f:
                    content=f.read(10000)
                    if f.read(1):
                        content += f'[...File "{file_path}" truncated at 10000 characters]'
                return content

        else:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: {e}'
