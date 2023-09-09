import sys

input_str = " ".join(sys.argv[1:])

if not input_str:
    input_str = input("Enter the cipher string: ")


def ceaser_shift(in_str: str, shift):
    if shift == 0:
        return in_str

    result = ""
    for i in in_str:
        if not i.isalpha():
            result += i
            continue

        is_upper = i.isupper()
        base = 65 if is_upper else 97
        new_chr = ord(i) - base + shift
        new_chr %= 26

        # print(f"{i}: {base}, {new_chr}")

        result += chr(new_chr + base)

    return result


print(f"Input: {input_str}")
for i in range(1, 26):
    print()
    print(f"{i}: {ceaser_shift(input_str, i)}")
