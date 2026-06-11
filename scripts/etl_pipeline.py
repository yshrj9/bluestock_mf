import subprocess
from pathlib import Path
rd = Path(__file__).parent.resolve()
scripts = [
    rd/"live_nav_fetch.py",
    rd/"load_db.py",
    rd/"recommender.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

print("All tasks completed.")
