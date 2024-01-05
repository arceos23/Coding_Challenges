# Write Your Own wc Tool

"[Write your own wc tool](https://codingchallenges.fyi/challenges/challenge-wc)" is the first challenge of [Coding Challenges](https://codingchallenges.fyi/challenges/intro), created by [John Crickett](https://www.linkedin.com/in/johncrickett/).

# Description

This wc tool (wc) is a simplified Unix [wc](https://man7.org/linux/man-pages/man1/wc.1.html) command line tool. wc receives standard input or file and option arguments from the command line. wc then displays to standard output the count metrics of the input based on the options given. If wc receives file arguments, the program displays file names at the end of their counts.

By default, wc displays the input's number of lines, words, and bytes. The following options augment the output of the program:

`-l`: Display the number of lines.

`-w`: Display the number of words.

`-c`: Display the number of bytes.

`-m`: Display the number of characters.

The program displays option-specified counts in this order: lines, words, bytes, and characters. An example command to display the line count of one file is: `python3 wc.py -l filename.txt`.

If wc receives more than one file, it will display count metrics and the name of each file on a separate line. The program finally displays count metric totals of all files. An example command to display the individual and total line counts for two files is: `python3 wc.py -l filename_0.txt filename_1.txt`.

If wc receives no files, it will provide counts based on standard input and any options provided. An example command of this is piping standard output from `cat` into wc: `cat filename.txt | python3 wc.py -l`.

wc can also provide details about the program and how to use it by running it with the `-h` or `--help` options. An example of this is: `python3 wc.py -h`.