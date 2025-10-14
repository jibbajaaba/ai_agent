import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    working_dir_abs = os.path.abspath(working_directory)

    if not full_path.startswith(working_dir_abs):
        raise Exception(f"Error: Cannot list {directory} as it is outside the permitted working directory.")
    
    if not os.path.exists(full_path):
        raise Exception(f'Error: The directory "{directory}" does not exist.')
    
    if not os.path.isdir(full_path):
        raise Exception(f'Error: "{directory}" is not a directory.')
    
    result = []
    
    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)

        file_size = os.path.getsize(item_path)

        is_dir = os.path.isdir(item_path)

        result.append(f"{item}: file_size={file_size} bytes, is_dir={is_dir}")

    print("\n".join(result))

