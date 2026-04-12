import Preprocessor
import Compiler
import Assembler
import sys
import os

def main():
    first_cmd_line_arg = 1
    file_to_compile : str | os.PathLike[str] = sys.argv[first_cmd_line_arg]
    file_to_compile = file_to_compile[:-2]
    pre_processed_file :  str | os.PathLike[str] = str(file_to_compile + '.p')
    Preprocessor.pre_proces_file(file_to_compile, pre_processed_file)
    Compiler.compile(pre_processed_file)
    compiled_file : str | os.PathLike[str]  = pre_processed_file[:-2] + '.s'
    executable_file : str | os.PathLike[str]  = pre_processed_file[:-2]
    Assembler.generate_assembly(compiled_file, executable_file)
    
if __name__=="__main__":
    main()