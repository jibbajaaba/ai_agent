import os

def get_file_content(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_abs = os.path.abspath(working_directory)

    if not full_path.startswith(working_dir_abs):
        raise Exception(f"Error: Cannot read {file_path} as it is outside the permitted working directory.")
    
    if not os.path.exists(full_path):
        raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
    
    if not os.path.isfile(full_path):
        raise Exception(f'Error: "{file_path}" is not a file.')
    
    MAX_CHARS = 10000

    with open(full_path, 'r') as file:
        file_content_string = file.read(MAX_CHARS + 1)

    if len(file_content_string) > MAX_CHARS:
        file_content_MAX_CHARS = file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        print(file_content_MAX_CHARS)
    else:
        print(file_content_string)