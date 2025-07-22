# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def process_line(line):
    operation, type_, words = line.strip().split(";")

    if operation == "S":  # Split
        if type_ == "M" and words.endswith("()"):
            words = words[:-2]  # Remove the '()' at the end

        result = ""
        for char in words:
            if char.isupper():
                result += " " + char.lower()
            else:
                result += char
        print(result.strip())

    elif operation == "C":  # Combine
        words_list = words.strip().split(" ")
        result = ""

        for i in range(len(words_list)):
            word = words_list[i]
            if type_ == "C" or (type_ in "MV" and i > 0):
                result += word.capitalize()
            else:
                result += word.lower()

        if type_ == "M":
            result += "()"

        print(result)

# Read input lines from standard input
for line in sys.stdin:
    if line.strip():  # Ignore empty lines
        process_line(line)
