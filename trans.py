#!/usr/bin/env python3

import parse_args
import subprocess

import get_file_type


def run():
    args = parse_args.parse()
    input_file = args.input_file
    input_type = get_file_type.get(input_file)
    output_type = args.output_type
    chain = planner.get_chain(input_file, input_type, output_type)
    executor.execute(chain)



if __name__ == "__main__":
    run()
