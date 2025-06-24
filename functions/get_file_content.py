import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        absp = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(absp, file_path))

        if not path.startswith(absp):
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(path):
             return f'Error: File not found or is not a regular file: "{file_path}"'
        
        file_content = None
        with open(path, "r") as f:
             file_content = f.read(MAX_CHARS)
             if len(f.read(MAX_CHARS)):
                  file_content += (f'[...File "{file_path}" truncated at 10000 characters]')
        
        return file_content
    except Exception as e:
        return f"Error: {e}"