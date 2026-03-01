import os

def process_file(file_path: bytes | os.PathLike) -> None:
    # Use os.fspath() to get a string or bytes representation
    path_str = os.fspath(file_path)
    with open(path_str, 'r') as f:
        print("Lexer running")
        pass

def run_analysis(file_path: bytes | os.PathLike) :
    
    process_file(file_path)