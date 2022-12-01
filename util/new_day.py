import sys
import os
import shutil
import fileinput
import requests
from pathlib import Path
from pprint import pprint
from bs4 import BeautifulSoup as bs

if len(sys.argv) < 2:
    print("No day number given")
    sys.exit()

YEAR = 2022
DAY  = int(sys.argv[1])


HERE = Path(__file__).parent
DAY_DIR = HERE.parent.joinpath(f"Day_{DAY}")

blank_py_file = os.path.join(HERE, "day_X.py")
data_dir = os.path.join(HERE, "data")


# Create DAY folder
os.makedirs(DAY_DIR)
assert(os.path.isdir(DAY_DIR))
print(f"Created new directory: {DAY_DIR}")

# Day file
new_py_file = DAY_DIR.joinpath(f"day_{DAY}.py")
shutil.copyfile(blank_py_file, new_py_file)
with fileinput.FileInput(new_py_file, inplace=True, backup='.bak') as py_file:
    for line in py_file:
        print(line.replace("day_X_input.txt", f"day_{DAY}_input.txt"), end='')
os.remove(os.path.join(DAY_DIR, f"day_{DAY}.py.bak"))
print(f"Created new python file: {new_py_file}")


# Create empty data .txt file
input_file = os.path.join(DAY_DIR, f"day_{DAY}_input.txt")
open(input_file, "a").close
print(f"Created empty file for input data: {input_file}")


# Get input data
with open(".env", "r") as f:
    cookie_session = f.read().strip()
    cookies_header = {'Cookie': cookie_session}

input_url = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"
res = requests.get(input_url, headers=cookies_header)
if res.status_code != 200:
    print(res.text)
    sys.exit()

# Write input to file
with open(input_file, "w") as f:
    f.write(res.text)

print("Wrote input data to file")
print("READY TO GO!")
