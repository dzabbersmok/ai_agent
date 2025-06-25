import os

from google.genai import types

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
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
    ),
)