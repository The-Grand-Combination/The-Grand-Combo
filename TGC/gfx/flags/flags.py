import os
import shutil

def copy_tga_files(directory):
    # Iterate over all files in the specified directory
    for filename in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), directory)):
        # Check if the file matches the 3-character .tga pattern
        if len(filename) == 7 and filename.endswith('.tga'):
            base_name = filename[:3]  # Extract the 3-character name
            original_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory, filename)
            
            # Create the three copies with new names
            copy1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory, f"{base_name}_dominion.tga")
            copy2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory, f"{base_name}_dominion2.tga")
            copy3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), directory, f"{base_name}_dominion3.tga")
            
            shutil.copyfile(original_file, copy1)
            shutil.copyfile(original_file, copy2)
            shutil.copyfile(original_file, copy3)
            
            print(f"Created copies: {copy1}, {copy2}, {copy3}")

# Set the directory path where your files are located
directory_path = 'flags'
copy_tga_files(directory_path)
