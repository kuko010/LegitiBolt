from pathlib import Path
import shutil
import subprocess

def move_item(src, dst):
    src_path = Path(src)
    dst_path = Path(dst)
    dst_path.mkdir(parents=True, exist_ok=True)

    target = dst_path / src_path.name
    if target.exists():
        if target.is_file():
            target.unlink()        # delete existing file
        else:
            shutil.rmtree(target)  # delete existing folder

    shutil.move(str(src_path), str(dst_path))

# Run git commands
cwd = "../legitieverything_data_pack"
subprocess.run(["git", "switch", "bolt"], cwd=cwd)
subprocess.run(["git", "add", "."], cwd=cwd)
subprocess.run(["git", "commit", "-m", "build"], cwd=cwd)
subprocess.run(["git", "push"], cwd=cwd)
subprocess.run(["rm", "-rf", "./code"], cwd=cwd)  # Linux/Mac

# Move items to temp
items = [".git", ".gitignore", "merge_only_beet.sh", "NOTE.md", "pack.mcmeta", "README.md"]
for item in items:
    move_item(f"../legitieverything_data_pack/{item}", "../temp")

# Run beet build
subprocess.run(["beet", "build"])

# Move items back
for item in items:
    move_item(f"../temp/{item}", "../legitieverything_data_pack")

# Optionally remove temp folder
shutil.rmtree("../temp")