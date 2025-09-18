import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-H", "--height", type=int, help="Height")
args = ap.parse_args()

print(args.height)