import os
import subprocess

def generate_assembly(COMPILED_FILE: str | os.PathLike[str], EXECUTABLE_FILE: str | os.PathLike[str]):
    subprocess.run(["gcc", f"{COMPILED_FILE}", "-O", f"{EXECUTABLE_FILE}"])
    subprocess.run(["rm", "-rf", "-O", f"{COMPILED_FILE}"])