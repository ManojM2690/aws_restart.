import re
sequence = "ORIGIN   1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn //"
clean_sequence = re.sub(r'[^a-zA-Z0-9]','',sequence)
print(clean_sequence)