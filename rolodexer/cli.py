#!/usr/bin/env python
"""rolodexer

Usage:
    rolodexer INFILE [-o OUTFILE] [-V | --verbose]
    rolodexer -h | --help | -v | --version

Options:
    -o OUTFILE          specify output file [default: stdout]
    -V --verbose        print verbose output
    -h --help           show this text
    -v --version        print version

"""

from __future__ import print_function
from docopt import docopt
import sys

def cli(argv):
    arguments = docopt(__doc__, argv=argv,
                                help=False,
                                version='0.1.0')
    print(argv)
    print(arguments)

if __name__ == '__main__':
    cli(sys.argv[1:])