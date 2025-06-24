import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        absp = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(absp, file_path))

        if not path.startswith(absp):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not path.endswith(".py"):
             return f'Error: "{file_path}" is not a Python file.'

        if not os.path.exists(path):
             return f'Error: File "{file_path}" not found.'
        
        result = subprocess.run(['python3', path], capture_output=True, text=True, timeout=30)
        return_code = result.returncode

        output = []

        if len(result.stdout) == 0 and len(result.stderr) == 0:
            return "No output produced."

        if len(result.stdout) > 0:
            output.append(f"STDOUT: {result.stdout.strip()}")

        if len(result.stderr) > 0:
            output.append(f"STDERR: {result.stderr.strip()}")

        if result.returncode != 0:
             output.append(f"Process exited with code {return_code}")
        
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"