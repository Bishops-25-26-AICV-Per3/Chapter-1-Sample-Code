import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-w", "--width", type=int, help="Width of output")
# DON'T USE -h!! That is reserved for help.
ap.add_argument("-H", "--height", type=int, help="Height of output")
args = ap.parse_args()

print(args)
print(args.image)
print(args.width)
print(args.height)

"""
With command line: (pr python3, YMMV)
python argparse_details.py --image x.png -w 50 -H 100

you should get:
Namespace(image='x.png', width=50, height=100)
x.png
50
100
"""