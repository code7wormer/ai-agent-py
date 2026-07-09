import os
import subprocess


def run_python_file(working_directory:str,file_path:str, args: list[str] | None =None)->str:
    try:
        work_abs=os.path.abspath(working_directory)
        abs_file_path=os.path.normpath(os.path.join(work_abs,file_path))
        within_scope=os.path.commonpath([work_abs,abs_file_path])==work_abs
        if not within_scope:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            if not os.path.isfile(abs_file_path):
                return f'Error: "{file_path}" does not exist or is not a regular file'
            elif not file_path.endswith(".py"):
                return f'Error: "{file_path}" is not a Python file'
            else:
                command = ["python", abs_file_path]
                if args is not None:
                    command.extend(args)
                result= subprocess.run(
                    command,
                    cwd=work_abs,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                output=[]
                if result.returncode !=0:
                    output.append(f'Process exited with code {result.returncode}\n')
                if not result.stderr and not result.stdout:
                    output.append("No output produced")
                else:
                    if result.stderr:
                        output.append(f'STDERR: {result.stderr}')
                    if result.stdout:
                        output.append(f'STDOUT: {result.stdout}')
                return "".join(output)


    except Exception as e:
        return f"Error: executing Python file: {e}"