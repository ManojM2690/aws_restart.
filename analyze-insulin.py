import re

sequence = """
ORIGIN   1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 
61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn //
"""

# Remove all non-alphanumeric characters and spaces from each line
clean_sequence = re.sub(r'[^a-zA-Z0-9\s]', '', sequence, flags=re.MULTILINE)

print(clean_sequence)
