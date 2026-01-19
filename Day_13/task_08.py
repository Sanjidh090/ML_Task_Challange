import os

try:
    folder_path = "/Download/sample_data"  # Example folder path
    file_name = "README.md"             # Example file name

    # Join folder and file into a full path
    full_path = os.path.join(folder_path, file_name)

    print("Full path:", full_path)

except Exception as e:
    print("Error:", e)

