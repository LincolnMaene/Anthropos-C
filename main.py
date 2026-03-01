from Lexical_analyzer import Lexer
import Tests.RegressionTester as Tester
import os
import sys
from pathlib import Path

def main():

    if ("-T" in sys.argv) or ('-t' in sys.argv):
        Tester.regression_test()
    try:

        fileCompiled : os.PathLike = Path(sys.argv[1])
        Lexer.run_analysis(fileCompiled)

    except IndexError:

        print("Error: no file file cmd line argument")

    except FileNotFoundError:

        print("File to compile not found")


if __name__ == "__main__":
    main()