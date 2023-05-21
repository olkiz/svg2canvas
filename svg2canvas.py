#!/bin/python3
import argparse
import sys
from enum import Enum
from svgelements import *
from PyTkConverter import PyTkConverter
from SwiftConverter import SwiftConverter

class ConverterType(Enum):
    pytkinter = 'python-tk'
    swiftuikit = 'swift-uikit'

    def __str__(self):
        return self.value

def arg_parser(argv):
    parser = argparse.ArgumentParser(description='Convert your svg to code.')
    parser.add_argument('-i', '--input-file', dest='input_file', type=str, help='file with svg')
    parser.add_argument('-o', '--output-file', dest='output_file', type=str, default='output', help='file to output code')
    parser.add_argument('-t', '--', dest='type', type=ConverterType, choices=ConverterType, default=ConverterType.pytkinter, help='type of canvas program')
    return parser.parse_args(argv[1:])

def main(argv) -> int:
    args = arg_parser(argv)
    converter = None
    openFileName = "file"
    match args.type:
        case ConverterType.pytkinter:
            converter = PyTkConverter()
            openFileName = args.output_file + ".py"
        case ConverterType.swiftuikit:
            converter = SwiftConverter()
            openFileName = args.output_file + ".swift"


    data = converter.convert(args.input_file)
    output_file = open(openFileName, "w")
    output_file.write(data)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
