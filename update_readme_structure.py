import os

README_PATH = "README.md"
START_TAG = "<!-- START_STRUCTURE -->"
END_TAG = "<!-- END_STRUCTURE -->"

def generate_tree(start_path="."):
    tree = []
    for root, dirs, files in os.walk(start_path):
        # skip .git and __pycache__
        dirs[:] = [d for d in dirs if d not in [".git", "__pycache__"]]

        level = root.replace(start_path, "").count(os.sep)
        indent = "│   " * (level - 1) + ("├── " if level > 0 else "")
        tree.append(f"{indent}{os.path.basename(root)}/")

        for f in files:
            tree.append(f"{'│   ' * level}├── {f}")

    return "```\n" + "\n".join(tree) + "\n```"


def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    tree_md = generate_tree()

    if START_TAG in readme and END_TAG in readme:
        before = readme.split(START_TAG)[0]
        after = readme.split(END_TAG)[1]
        new_readme = before + START_TAG + "\n" + tree_md + "\n" + END_TAG + after
    else:
        # If tags are missing, append at bottom
        new_readme = readme + "\n\n" + START_TAG + "\n" + tree_md + "\n" + END_TAG

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

    print("README updated with latest directory structure!")


if __name__ == "__main__":
    update_readme()
