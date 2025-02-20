import os
import shutil

def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def sort_files(directory):
    """Sort files in the specified directory into subdirectories based on file type."""
    # Change to the target directory
    os.chdir(directory)

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(filename):
            continue
        
        # Get the file extension
        file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
        
        # Create a directory for the file type if it doesn't exist
        create_directory(file_extension)
        
        # Move the file into the corresponding directory
        shutil.move(filename, os.path.join(file_extension, filename))
        print(f'Moved: {filename} -> {file_extension}/')

def main():
    print("Welcome to the Advanced File Manager!")
    directory = input("Enter the path of the directory to sort files: ")

    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return

    sort_files(directory)
    print("Files have been sorted successfully!")

if __name__ == "__main__":
    main()
