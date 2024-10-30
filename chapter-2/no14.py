#14. First N lines
#Receive a natural number $N$ from a command-line argument, and output the first $N$ lines of the file. Confirm the result by using head command.
import sys
import pandas as pd

try:
    if len(sys.argv) < 2:
        raise ValueError

    N = int(sys.argv[1])

except ValueError:
    print("Error: Please specify a natural number N.")
    sys.exit(1)

data = pd.read_table('popular-names.txt', names=["name", "sex", "cnt", "year"])

print(data.head(N))