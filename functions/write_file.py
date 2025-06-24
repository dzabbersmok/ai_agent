import os

def write_file(working_directory, file_path, content):
    try:
        absp = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(absp, file_path))

        if not path.startswith(absp):
                return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # print(os.path.exists(path))
        if not os.path.exists(path):
             folder_path = os.path.dirname(path)
             os.makedirs(folder_path, exist_ok=True)

        with open(path, "w") as f:
            f.write(content)
    
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
