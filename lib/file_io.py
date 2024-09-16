from pathlib import Path

def write_file(file_name, file_content, extension='.txt'):
  
    # Ensure file_name is a Path object
    file_path = Path(file_name).with_suffix(extension)
    
    try:
        with file_path.open('w') as file:
            file.write(file_content)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def append_file(file_name, file_content, extension='.txt'):
    
    # Ensure file_name is a Path object
    file_path = Path(file_name).with_suffix(extension)
    
    try:
        with file_path.open('a') as file:
            file.write(file_content)
    except IOError as e:
        print(f"An error occurred while appending to the file: {e}")

def read_file(file_name, extension='.txt'):
   
    # Ensure file_name is a Path object
    file_path = Path(file_name).with_suffix(extension)
    
    try:
        with file_path.open('r') as file:
            return file.read()
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return ""
