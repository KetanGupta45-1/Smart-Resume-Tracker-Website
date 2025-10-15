import os

# Directories to include
directories = ["Core__", "Improvement__", "Matching__", "Models__", "Utility__"]

# Individual files to include
extra_files = ["imp.py", "main.py", "call_matching.py"]

# Output file name
output_file = "all_project_code.txt"

def collect_code(base_path="."):
    collected_data = []

    # Traverse through each main directory
    for folder in directories:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".py"):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, "r", encoding="utf-8") as f:
                                code = f.read()
                            collected_data.append(f"\n\n### DIRECTORY: {folder}\n### FILE: {file}\n\n{code}\n")
                        except Exception as e:
                            collected_data.append(f"\n\n### DIRECTORY: {folder}\n### FILE: {file}\n\n[Error reading file: {e}]\n")
    
    # Add extra specified files
    for file in extra_files:
        file_path = os.path.join(base_path, file)
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()
                collected_data.append(f"\n\n### FILE: {file}\n\n{code}\n")
            except Exception as e:
                collected_data.append(f"\n\n### FILE: {file}\n\n[Error reading file: {e}]\n")

    # Combine and save all code into one text file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(collected_data))

    print(f"✅ Code collected successfully and saved to '{output_file}'")


if __name__ == "__main__":
    collect_code()
