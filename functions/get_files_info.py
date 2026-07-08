import os

def get_files_info(working_directory:str , directory:str = "."):
    try:
        work_abs=os.path.abspath(working_directory)
        target_dir=os.path.normpath(os.path.join(work_abs,directory))
        within_scope=os.path.commonpath([work_abs,target_dir])==work_abs
        if not within_scope:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            if not os.path.isdir(target_dir):
                return f'Error: "{directory}" is not a directory'
            else:
                # return f'Success: "{directory}" is within the working directory'
                print(f"Result for {directory} directory")
                lst=[]
                for item in os.listdir(target_dir):
                    item_path=os.path.join(target_dir,item)
                    size=os.path.getsize(item_path)
                    is_dir="False" if not os.path.isdir(item_path) else "True"
                    lst.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
                return "\n".join(lst)



    except Exception as e:
        return f"Error: {e}"
