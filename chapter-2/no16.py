#16. Split a file into N pieces
#Receive a natural number $N$ from a command-line argument, and split the input file into $N$ pieces at line boundaries. Confirm the result by using split command.

import sys
import pandas as pd

try:
    if len(sys.argv) < 2:
        raise ValueError

    N = int(sys.argv[1])

except ValueError:
    print("Error: Please specify a natural number N.")
    sys.exit(1)

data = pd.read_table('popular-names.txt', names=["name", "sex", "num", "year"])
parts = [data.iloc[i:i + N] for i in range(0, len(data), N)]

for i, part in enumerate(parts):
    print(f"=== {i + 1} ===")
    print(part)
    print()