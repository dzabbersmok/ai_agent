import os

from google.genai import types

def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
             directory = ""

        absp = os.path.abspath(working_directory)
        dir_path = os.path.abspath(os.path.join(absp, directory))

        if not dir_path.startswith(absp):
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(dir_path):
            return f'Error: "{directory}" is not a directory'
        
        directory_list = os.listdir(dir_path)

        if len(directory_list) > 0:
            all_files = []
            for file in directory_list:
                path = os.path.join(dir_path, file)
                size = os.path.getsize(path)
                is_dir = os.path.isdir(path)
                all_files.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")

            return "\n".join(all_files)
        else:
            return "Selected directory is empty"
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)