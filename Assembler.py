import os
import subprocess
import pydoc
def generate_assembly(COMPILED_FILE: str | os.PathLike[str], EXECUTABLE_FILE: str | os.PathLike[str]):
    '''
    Generates assembly code from a compiled file and creates an executable.
    Args:
        COMPILED_FILE (str | os.PathLike[str]): The path to the compiled file.
        EXECUTABLE_FILE (str | os.PathLike[str]): The path to the output executable file.
    '''
    subprocess.run(["gcc", f"{COMPILED_FILE}", "-O", f"{EXECUTABLE_FILE}"])
    subprocess.run(["rm", "-rf", "-O", f"{COMPILED_FILE}"])

pydoc.writedoc('Assembler')