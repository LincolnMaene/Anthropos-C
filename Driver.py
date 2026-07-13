import Preprocessor
import Compiler.Compiler as Compiler
import Compiler.Compiler_Errors as Compiler_Errors
import Assembler
import sys
import os

def main():
    # first command line argument, i expect this to be the c file to compile
    first_cmd_line_arg = 1
    file_to_compile : str | os.PathLike[str] = sys.argv[first_cmd_line_arg]
    #output of gcc -E -P file_to_compile -o pre_processed_file
    pre_processed_file :  str | os.PathLike[str] = str(file_to_compile[:-1] + 'i')
    Preprocessor.pre_proces_file(file_to_compile, pre_processed_file)
    
    if Compiler.compile(pre_processed_file) == Compiler_Errors.success:
        compiled_file : str | os.PathLike[str]  = pre_processed_file[:-2] + '.s'
        executable_file : str | os.PathLike[str]  = pre_processed_file[:-2]
        Assembler.generate_assembly(compiled_file, executable_file)
    else:
        print("Compilation failed.")
    
if __name__=="__main__":
    main()