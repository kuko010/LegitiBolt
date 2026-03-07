from pathlib import Path
import shutil
from send2trash import send2trash
import subprocess
import argparse
from datetime import datetime  # <-- added for timestamp

parser = argparse.ArgumentParser()
parser.add_argument("--merge", action="store_true")
parser.add_argument("--commit", action="store_true")
args = parser.parse_args()

def move_item(src, dst):
    src_path = Path(src)
    dst_path = Path(dst)
    dst_path.mkdir(parents=True, exist_ok=True)

    target = dst_path / src_path.name
    if target.exists():
        send2trash(str(target))

    shutil.move(str(src_path), str(dst_path))

# Helper to get current timestamp string
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Run git commands
cwd = "../legitieverything_data_pack"
subprocess.run(["git", "switch", "bolt"], cwd=cwd, check=True)
subprocess.run(["git", "add", "."], cwd=cwd, check=True)

# First commit with timestamp
commit_msg1 = f"build at {get_timestamp()}"
subprocess.run(["git", "commit", "-m", commit_msg1], cwd=cwd)

subprocess.run(["git", "push"], cwd=cwd, check=True)
code_path = Path(cwd) / "code"
if code_path.exists():
    shutil.rmtree(str(code_path))

# Move items to temp
items = [".git", ".gitignore", "merge_only_beet.sh", "NOTE.md", "pack.mcmeta", "README.md", "1.21.10"]
for item in items:
    move_item(f"../legitieverything_data_pack/{item}", "../temp")

try:
    subprocess.run(["beet", "build"], check=True)
except Exception as e:
    print(f"Build failed: {e}")
finally:
    for item in items:
        move_item(f"../temp/{item}", "../legitieverything_data_pack")
    shutil.rmtree("../temp")

if args.commit:
    subprocess.run(["git", "add", "."], cwd=cwd, check=True)

    # Second commit with timestamp
    commit_msg2 = f"build at {get_timestamp()}"
    subprocess.run(["git", "commit", "-m", commit_msg2], cwd=cwd, check=True)

    subprocess.run(["git", "push"], cwd=cwd, check=True)

    if args.merge:
        subprocess.run("merged", cwd="../", shell=True)