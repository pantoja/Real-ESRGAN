import shutil

file_path = "/usr/local/lib/python3.11/dist-packages/basicsr/data/degradations.py"
copied_file_path = (
    "/usr/local/lib/python3.10/dist-packages/basicsr/data/degradations_backup.py"
)


def copy_file(file_path, copied_file_path):
    shutil.copy(file_path, copied_file_path)


def rewrite_file(file_path):
    # Read the file
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Modify line 8 (index 7 because line numbers start at 1)
    lines[7] = "from torchvision.transforms.functional import rgb_to_grayscale\n"

    # Write the modified content back to the file
    with open(file_path, "w") as f:
        f.writelines(lines)

    print(f"Line 8 in {file_path} has been updated.")


if __name__ == "__main__":
    copy_file(file_path, copied_file_path)
    rewrite_file(file_path)
