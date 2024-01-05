import unittest
import subprocess

# Command line arguments
PYTHON3 = 'python3'
WC_FILE = 'wc.py'
CAT_UTL = 'cat'
TEST_FILE = 'test.txt' # Also an output

# Command line options
OPT = '-'
CHAR_FLAG = 'm'
LINE_FLAG = 'l'
BYTE_FLAG = 'c'
WORD_FLAG = 'w'

# Outputs
LINE_COUNT = 7145
CHAR_COUNT = 339292
BYTE_COUNT = 342190
WORD_COUNT = 58164
TOTAL = 'total'
NEW_LINE = '\n'

# Decodings
BYTE_DECODING = 'utf-8'


class Test_wc(unittest.TestCase):
    # Input of a single file
    def test_no_opt_one_file_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{LINE_COUNT} {WORD_COUNT} {BYTE_COUNT} {TEST_FILE}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_line_opt_one_file_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + LINE_FLAG, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{LINE_COUNT} {TEST_FILE}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_char_opt_one_file_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + CHAR_FLAG, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{CHAR_COUNT} {TEST_FILE}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_byte_opt_one_file_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + BYTE_FLAG, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{BYTE_COUNT} {TEST_FILE}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_word_opt_one_file_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + WORD_FLAG, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{WORD_COUNT} {TEST_FILE}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    # Input of multiple files
    def test_no_opt_two_files_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, TEST_FILE, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'''{LINE_COUNT} {WORD_COUNT} {BYTE_COUNT} {TEST_FILE}{NEW_LINE}{LINE_COUNT} {WORD_COUNT} {BYTE_COUNT} {TEST_FILE}{NEW_LINE}{LINE_COUNT * 2} {WORD_COUNT * 2} {BYTE_COUNT * 2} {TOTAL}{NEW_LINE}''',
                         result.stdout.decode(BYTE_DECODING))

    def test_line_opt_two_files_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + LINE_FLAG, TEST_FILE, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{LINE_COUNT} {TEST_FILE}{NEW_LINE}{LINE_COUNT} {TEST_FILE}{NEW_LINE}{LINE_COUNT * 2} {TOTAL}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_char_opt_two_files_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + CHAR_FLAG, TEST_FILE, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{CHAR_COUNT} {TEST_FILE}{NEW_LINE}{CHAR_COUNT} {TEST_FILE}{NEW_LINE}{CHAR_COUNT * 2} {TOTAL}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_byte_opt_two_files_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + BYTE_FLAG, TEST_FILE, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{BYTE_COUNT} {TEST_FILE}{NEW_LINE}{BYTE_COUNT} {TEST_FILE}{NEW_LINE}{BYTE_COUNT * 2} {TOTAL}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_word_opt_two_files_count(self):
        result = subprocess.run([PYTHON3, WC_FILE, OPT + WORD_FLAG, TEST_FILE, TEST_FILE],
                                capture_output=True)
        self.assertEqual(f'{WORD_COUNT} {TEST_FILE}{NEW_LINE}{WORD_COUNT} {TEST_FILE}{NEW_LINE}{WORD_COUNT * 2} {TOTAL}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    # Input of standard input
    def test_no_opt_stdin_count(self):
        cat_result = subprocess.run(["cat", "test.txt"],
                                    capture_output=True)
        result = subprocess.run([PYTHON3, WC_FILE],
                                input=cat_result.stdout,
                                capture_output=True)
        self.assertEqual(f'{LINE_COUNT} {WORD_COUNT} {BYTE_COUNT}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_line_opt_stdin_count(self):
        cat_result = subprocess.run(["cat", "test.txt"],
                                    capture_output=True)
        result = subprocess.run([PYTHON3, WC_FILE, OPT + LINE_FLAG],
                                input=cat_result.stdout,
                                capture_output=True)
        self.assertEqual(f'{LINE_COUNT}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_char_opt_stdin_count(self):
        cat_result = subprocess.run(["cat", "test.txt"],
                                    capture_output=True)
        result = subprocess.run([PYTHON3, WC_FILE, OPT + CHAR_FLAG],
                                input=cat_result.stdout,
                                capture_output=True)
        self.assertEqual(f'{CHAR_COUNT}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_byte_opt_stdin_count(self):
        cat_result = subprocess.run(["cat", "test.txt"],
                                    capture_output=True)
        result = subprocess.run([PYTHON3, WC_FILE, OPT + BYTE_FLAG],
                                input=cat_result.stdout,
                                capture_output=True)
        self.assertEqual(f'{BYTE_COUNT}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

    def test_word_opt_stdin_count(self):
        cat_result = subprocess.run(["cat", "test.txt"],
                                    capture_output=True)
        result = subprocess.run([PYTHON3, WC_FILE, OPT + WORD_FLAG],
                                input=cat_result.stdout,
                                capture_output=True)
        self.assertEqual(f'{WORD_COUNT}{NEW_LINE}',
                         result.stdout.decode(BYTE_DECODING))

if __name__ == '__main__':
    unittest.main()
