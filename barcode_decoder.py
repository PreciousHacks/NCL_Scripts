import sys

from pyzbar.pyzbar import decode
from PIL import Image

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <image_path>")
    print("Include image path! Exiting... ")
    sys.exit(1)

input_str = sys.argv[1]


for i in decode(Image.open(input_str)):
    print(i)
