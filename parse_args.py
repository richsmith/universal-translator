import argparse

def parse():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("output_type", type=str,
                        help="the file type to ouput")
    parser.add_argument("input_file", 
                        help="the file to convert")
    parser.add_argument("--verbosity", "-v", help="increase output verbosity")
    args = parser.parse_args()
    return args

