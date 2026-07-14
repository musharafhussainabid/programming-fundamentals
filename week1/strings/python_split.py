"""
In industrial production, data rarely arrives beautifully packaged. It comes as raw, 
concatenated streams of text-logs, CSV files, payload headers, or CLI inputs.
.split() is the primary too engineers use to chop those raw streams into structured, accessible pieces.
"""

#1. What is Python split()?
#At its core, .split() takes a single string and cuts it into a list of substrings based on a specified delimiter (separator).

description:str = "Hello Google, I am Musharaf Hussain Abid, an AI Engineer with 1.5+ years of industrial experience"
#The Syntax
#string.split(separator=None, maxsplit=-1)
#separator (or delimiter): The pattern where the split should happen. 
# If you don't specify one (or pass None), 
# Python defaults to splitting by any run of whitespace (spaces, tabs, newlines) 
# and automatically groups consecutive spaces together.
#maxsplit: How many cuts to make. The default is -1, which means "cut as many times as possible."


#Behavior A: Splitting by Whitespace (Default)
splitted_descritions: list = description.split(None, maxsplit=-1)
print(splitted_descritions)

#Behavior B: Splitting by an Explicit Delimiter
summary : str = "The match has been ended, both teams performed well, but the one with high self confidence, team-work, and pressure handling ability won!"
splitted_summary : list = summary.split(",", maxsplit=-1)
print(splitted_summary)

summary : str = "The match has been ended, both teams performed well, but the one with high self confidence, team-work, and pressure handling ability won!"
_summary : list = summary.split("e", maxsplit=-1)#the char 'e' will be stripped and rest of the list of strings will be printed without 'e';
print(_summary)



#3. Real Production Use Cases at Scale
#In production code, developers rely on .split() for three major tasks:

# Use Case A: Parsing CSV/TSV Flat Files

def stream_and_parse_csv(file_path: str):
    with open(file_path, mode="r", encoding="utf-8") as file:
        header = file.readline().strip().split(",") # We use .strip() to clean up the trailing newline '\n' before splitting
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            row_values = clean_line.split(",")
            yield dict(zip(header, row_values))



total_revenue_for_completed : float = 0.0
file_path = "week1/strings/data/transactions.csv"

for record in stream_and_parse_csv(file_path):
    if record["status"] == "COMPLETED":
        total_revenue_for_completed += float(record["amount"])


print(f"The total amount for The Completed Transaction is: ${total_revenue_for_completed:,.2f}")

#Why this is highly efficient:Constant Memory Footprint ($O(1)$ Space Complexity):
#  Because we use a generator (yield), we don't build a massive list of dictionaries. 
# We read a line, split it, calculate, and instantly throw it away when the loop moves to the next line.
# Double Team (.strip() + .split()): Notice the line file.readline().strip().split(","). 
# If we didn't use .strip() first, the last item (timestamp) would look like "2026-07-14T08:30:00Z\n" instead of "2026-07-14T08:30:00Z".
# ⚠️ The "Gotcha" with raw .split(",") in CSVs:
# If a CSV field contains text with an actual comma in it (e.g., "Hussain, Musharaf"), 
# a simple .split(",") will break because it thinks the comma inside the quotes is a column boundary.
# If your CSV data has quoted text with commas inside it, a Google engineer won't write a custom regex.
#  Instead, they will use Python's built-in, highly-optimized csv module, which does the splitting safely under the hood:
#import csv
# reader = csv.DictReader(file)

