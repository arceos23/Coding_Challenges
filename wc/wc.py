import argparse
import os
import sys
from collections import defaultdict, deque

# Encodings of count metrics to options
BYTES = 'c'
LINES = 'l'
CHARS = 'm'
WORDS = 'w'

# Output summary
TOTAL = 'total'

''' Minimum number of command line arguments present if multiple files given
based on if options were provided '''
MIN_NUM_ARGS_NO_OPTS = 2
MIN_NUM_ARGS_W_OPT = 3

def get_counts(file):
    num_lines = num_words = num_bytes = num_chars = 0
    for line in file:
        num_lines += 1
        num_words += len(line.split())
        num_bytes += len(line)
        num_chars += len(line.decode())
    return num_lines, num_words, num_bytes, num_chars

def get_output_line(*args):
    return ' '.join(str(arg) for arg in args)

def print_wc_output(wc_output):
    for line in wc_output:
        print(line)

def word_count():
    parser = argparse.ArgumentParser(prog="wc",
                                    description="""A simple wc utility that
                                    displays the number of lines, words,
                                    bytes, or characters contained in each,
                                    input file, or standard input (if no file
                                    is specified) to the standard output.""")
    parser.add_argument("files", nargs="*", default=sys.stdin)
    parser.add_argument("-l",
                        help="""The number of lines in each input file is
                        written to the standard output.""",
                        action="store_true")
    parser.add_argument("-c",
                        help="""The number of bytes in each input file is
                        written to the standard output.""",
                        action="store_true")
    parser.add_argument("-w",
                        help="""The number of words in each input file is
                        written to the standard output.""",
                        action="store_true")
    parser.add_argument("-m",
                        help="""The number of characters in each input file
                        is written to the standard output.""",
                        action="store_true")
    args = parser.parse_args()

    def has_option():
        return args.c or args.l or args.m or args.w

    def got_multiple_files_no_options():
        return len(sys.argv) > MIN_NUM_ARGS_NO_OPTS and not has_option()

    def got_multiple_files_options():
        return len(sys.argv) > MIN_NUM_ARGS_W_OPT and has_option()

    def received_multiple_files():
        return got_multiple_files_no_options() or got_multiple_files_options()

    def get_wc_line(num_lines, num_words, num_bytes, num_chars, line_name):
        line = []
        if args.l:
            line.append(get_output_line(num_lines))
        if args.w:
            line.append(get_output_line(num_words))
        if args.c:
            line.append(get_output_line(num_bytes))
        if args.m:
            line.append(get_output_line(num_chars))
        if not has_option():
            line.append(get_output_line(num_lines,
                                        num_words,
                                        num_bytes))
        if line_name:
            line.append(line_name)
        return ' '.join(line)

    def update_option_totals(num_lines, num_words, num_bytes, num_chars):
        if args.l:
            option_to_total[LINES] += num_lines
        if args.w:
            option_to_total[WORDS] += num_words
        if args.c:
            option_to_total[BYTES] += num_bytes
        if args.m:
            option_to_total[CHARS] += num_chars
        if not has_option():
            option_to_total[LINES] += num_lines
            option_to_total[WORDS] += num_words
            option_to_total[BYTES] += num_bytes

    # Prepare files for processing based on input received
    files = None
    if args.files == sys.stdin:
        files = [args.files]
    else:
        files = args.files

    # Build wc output
    option_to_total = defaultdict(int)
    wc_output = deque()
    for file in files:
        # Get parts of output line
        line_name, counts = None, None
        if args.files == sys.stdin:
            counts = get_counts(sys.stdin.buffer)
        else:
            absolute_path = os.path.dirname(__file__)
            full_path = os.path.join(absolute_path, file)
            line_name = file

            with open(full_path, 'rb') as f:
                counts = get_counts(f)

        # Create output line
        num_lines, num_words, num_bytes, num_chars = counts
        wc_output.append(get_wc_line(num_lines,
                                     num_words,
                                     num_bytes,
                                     num_chars,
                                     line_name))

        # Update totals if multiple files received
        if received_multiple_files():
            update_option_totals(num_lines, num_words, num_bytes, num_chars)

    # Create totals output line if multiple files received
    if len(files) > 1:
        wc_output.append(get_wc_line(option_to_total[LINES],
                                     option_to_total[WORDS],
                                     option_to_total[BYTES],
                                     option_to_total[CHARS],
                                     TOTAL))

    print_wc_output(wc_output)

if __name__ == "__main__":
    word_count()