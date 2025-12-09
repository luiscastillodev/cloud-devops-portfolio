import os

def generate_tree(start_path, prefix=""):
    tree = ""
    items = sorted(os.listdir(start_path))

    for index, item in enumerate(items):
        path = os.path.join(start_path, item)

        # Skip unwanted directories or files
        if item in [".git", "__pycache__", ".DS_Store"]:
            continue

        connector = "├── " if index < len(items) - 1 else "└── "
        tree += f"{prefix}{connector}{item}\n"

        if os.path.isdir(path):
            extension = "│   " if index < len(items) - 1 else "    "
            tree += generate_tree(path, prefix + extension)

    return tree

def update_readme():
    readme_path = "README.md"

    # Read README in UTF-8
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Locate tree section markers
    start_marker = "<!-- TREE_START -->"
    end_marker = "<!-- TREE_END -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("ERROR: README missing TREE_START or TREE_END markers.")
        return

    # Generate new tree
    tree_output = "```\n" + generate_tree(".") + "```\n"

    # Replace existing tree section
    new_content = (
        content[: start_idx + len(start_marker)] +
        "\n" + tree_output + "\n" +
        content[end_idx:]
    )

    # Write README in UTF-8
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print("README structure updated successfully.")

if __name__ == "__main__":
    update_readme()
