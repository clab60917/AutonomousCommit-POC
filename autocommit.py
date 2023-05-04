import os
import random
import subprocess
import time
from datetime import datetime

REPO_PATH = "/Users/clementarthaud/Documents/VSCODE/PERSO/AutonomousCommit-POC"

os.chdir(REPO_PATH)

def make_commit():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("commit.txt", "a") as f:
        f.write(f"{date}\n")

    subprocess.run(["git", "add", "commit.txt"])
    subprocess.run(["git", "commit", "-m", f"Mise à jour automatique : {date}"])
    subprocess.run(["git", "push", "origin", "main"])

num_commits = random.randint(1, 3)

for _ in range(num_commits):
    make_commit()
    time.sleep(random.randint(0, 3600))
