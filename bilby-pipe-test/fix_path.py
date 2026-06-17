from pathlib import Path
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument(
    "--file",
    default="test.ini",
    help="INI file to modify (default: test.ini)",
)

parser.add_argument(
    "--home",
    default=str(Path.home()),
    help=f"Replacement home directory (default: {Path.home()})",
)

args = parser.parse_args()

with open(args.file, "r") as f:
    text = f.read()

# Replace any /home/<username> with the requested home directory
text = re.sub(
    r"/home/[^/]+",
    args.home.rstrip("/"),
    text,
)

with open(args.file, "w") as f:
    f.write(text)

print(f"Updated {args.file}")
print(f"Using home directory: {args.home}")
