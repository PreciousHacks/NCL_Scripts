import sys

input_str = " ".join(sys.argv[1:])

if not input_str:
    input_str = input("Enter the input string: ")

result = ""

for i in input_str:
    if not i.isalpha():
        result += i
        continue

    is_upper = i.isupper()
    base = 65 if is_upper else 97

    new_chr = ord(i) - base
    new_chr = 25 - new_chr

    result += chr(new_chr + base)

print(result)