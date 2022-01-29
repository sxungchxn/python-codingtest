# croatia alphabet : c=, c-,
# dz=, d-,
# lj,
# nj,
# s=,
# z=
import sys

input_line = sys.stdin.readline().rstrip()

pos = 0
word = 0

while(pos < len(input_line)):
    if pos < len(input_line) - 1:
        if input_line[pos] == 'c':
            if input_line[pos+1] == '=' or input_line[pos + 1] == '-':
                pos += 1
        elif input_line[pos] == 'd':
            if input_line[pos+1] == 'z' and (pos + 2) < len(input_line) and input_line[pos + 2] == '=':
                pos += 2
            elif input_line[pos+1] == '-':
                pos += 1
        elif input_line[pos] == 'l' or input_line[pos] == 'n':
            if input_line[pos + 1] == 'j':
                pos += 1
        elif input_line[pos] == 's' or input_line[pos] == 'z':
            if input_line[pos+1] == '=':
                pos += 1
    pos += 1
    word += 1


print(word)
