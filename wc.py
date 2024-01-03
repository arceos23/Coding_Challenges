import argparse
import os
import sys
from collections import defaultdict, deque

# Encoding of count metric to option
BYTES = 'c'
LINES = 'l'
CHARS = 'm'
WORDS = 'w'

TOTAL = 'total'

''' Minimum number of command line arguments present if multiple files given
based on if options were provided '''
MIN_NUM_ARGS_MUL_FILES_NO_OPT = 2
MIN_NUM_ARGS_MUL_FILES_OPT = 3

def get_counts(file):
    num_chars = num_words = num_bytes = num_lines = 0
    for line in file:
        num_chars += len(line.decode())
        num_chars += len(line)
        num_words += len(line.split())
        num_bytes += len(line)
        num_lines += 1
    return num_chars, num_words, num_bytes, num_lines

def get_output_line(*args):
    return ' '.join(str(arg) for arg in args)

def print_output(output):
    for line in output:
        print(line)

def word_count():
    parser = argparse.ArgumentParser(prog="wc",
                                    description="""A simple wc utility that
                                    displays the number of lines, words,
                                    and bytes contained in each input
                                    file, or standard input (if no file is
                                    specified) to the standard output.""")
    parser.add_argument("files", nargs="*", default=sys.stdin)
    parser.add_argument("-l",
                        help="""The number of lines in the input file is
                        written to the standard output.""",
                        action="store_true")
    parser.add_argument("-c",
                        help="""The number of bytes in the input file is
                        written to the standard output.""",
                        action="store_true")
    parser.add_argument("-w",
                        help="""The number of words in the input file is
                        written to the standard output.""",
                        action="store_true")
    parser.add_argument("-m",
                        help="""The number of characters in the input file
                        is written to the standard output.""",
                        action="store_true")
    args = parser.parse_args()

    def has_opt():
        return args.c or args.l or args.m or args.w

    output = deque()

    def get_std_in_word_count():
        num_chars, num_words, num_bytes, num_lines = \
            get_counts(sys.stdin.buffer)
        line = []
        if args.c:
            line.append(get_output_line(num_bytes))
        if args.l:
            line.append(get_output_line(num_lines))
        if args.m:
            line.append(get_output_line(num_chars))
        if args.w:
            line.append(get_output_line(num_words))
        if not has_opt():
            line.append(get_output_line(num_lines, num_words, num_bytes))
        output.append(' '.join(line))

    def get_files_word_count():
        # Get the counts based on the given options for each file
        arg_to_total = defaultdict(int)
        for file in args.files:
            absolute_path = os.path.dirname(__file__)
            full_path = os.path.join(absolute_path, file)

            with open(full_path, 'rb') as f:
                num_chars, num_words, num_bytes, num_lines = get_counts(f)
                line = []
                if args.c:
                    arg_to_total[BYTES] += num_bytes
                    line.append(get_output_line(num_bytes))
                if args.l:
                    arg_to_total[LINES] += num_lines
                    line.append(get_output_line(num_lines))
                if args.m:
                    arg_to_total[CHARS] += num_chars
                    line.append(get_output_line(num_chars))
                if args.w:
                    arg_to_total[WORDS] += num_words
                    line.append(get_output_line(num_words))
                if not has_opt():
                    arg_to_total[LINES] += num_lines
                    arg_to_total[WORDS] += num_words
                    arg_to_total[BYTES] += num_bytes
                    line.append(get_output_line(num_lines,
                                                num_words,
                                                num_bytes))
                line.append(file)
                output.append(' '.join(line))

        # Include count totals of files if multiple files given
        line = []
        if (not has_opt() and len(sys.argv) > MIN_NUM_ARGS_MUL_FILES_NO_OPT or
            has_opt() and len(sys.argv) > MIN_NUM_ARGS_MUL_FILES_OPT):
            if args.c:
                line.append(get_output_line(arg_to_total[BYTES]))
            if args.l:
                line.append(get_output_line(arg_to_total[LINES]))
            if args.m:
                line.append(get_output_line(arg_to_total[CHARS]))
            if args.w:
                line.append(get_output_line(arg_to_total[WORDS]))
            if not has_opt():
                line.append(get_output_line(arg_to_total[LINES],
                                            arg_to_total[WORDS],
                                            arg_to_total[BYTES]))
            line.append(TOTAL)
            output.append(' '.join(line))

    if args.files == sys.stdin:
        get_std_in_word_count()
    else:
        get_files_word_count()

    print_output(output)

if __name__ == "__main__":
    word_count()