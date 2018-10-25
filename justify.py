# Justify. Distribute the text evenly between the margins.
 
import sys

# define default width
INPUT_WIDTH = 30 

# read inputs
if len(sys.argv) > 2:
    print("Usage: python justify.py width(optional)\n")
    exit()
if len(sys.argv) == 2:
    width = int(sys.argv[1])
else:
    width = INPUT_WIDTH 

words = open("text.txt", "r").read().split()
n = len(words)
outputs = list()

char_count = 0
word_count = 0
output = list() 

for i in range(n + 1):
    if i < n:
        word = words[i]
    if i == n or char_count + word_count + len(word) > width:
        total_spaces = width - char_count
        if word_count == 1:
            num_space_per_gap = 1
            res_spaces = total_spaces
        else:
            num_space_per_gap = total_spaces // (word_count - 1)
            res_spaces = total_spaces % (word_count - 1)
        spaces = list()
        for count in range(word_count - 1):
            space = " " * num_space_per_gap
            if res_spaces:
                space += " "
                res_spaces -= 1
            spaces.append(space)

        line = ""
        for j, w in enumerate(output):
            line += w
            if j < word_count - 1:
                line += spaces[j]
        outputs.append(line)     
        if i != n:
            output.clear()
            output.append(word)
            char_count = len(word)
            word_count = 1
    else:
        char_count += len(word)
        output.append(word)
        word_count += 1

for output in outputs:
    print(output)
