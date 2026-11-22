import os
import subprocess
import pydoc

def pre_proces_file(INPUT_FILE: str | os.PathLike[str], PRE_PROCESSED_FILE: str | os.PathLike[str]) -> None:
    '''
    Preprocesses the input file using gcc and generates a preprocessed file.
    '''
    subprocess.run(["gcc", "-E", "-P", INPUT_FILE, "-o", PRE_PROCESSED_FILE])

pydoc.writedoc('Preprocessor')