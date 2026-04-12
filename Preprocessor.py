import os
import subprocess

def pre_proces_file(INPUT_FILE: str | os.PathLike[str], PRE_PROCESSED_FILE: str | os.PathLike[str]) -> None:
    subprocess.run(["gcc", "-E", "-P", INPUT_FILE, "-O", PRE_PROCESSED_FILE])
