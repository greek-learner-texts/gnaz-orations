#!/usr/bin/env python3

"""
converts the extracted files from OGL into a textpart-per-chapter format.
"""

import unicodedata

for n in ["27", "28", "29", "30", "31"]:

    input_filename = f"text/orat{n}.txt"
    output_filename = f"text/orat{n}.chap.txt"

    with open(input_filename) as f, open(output_filename, "w") as g:
        chapter = 0
        text = []
        for line in f:
            line = unicodedata.normalize("NFC", line.strip())
            if line == "":  # blank line
                pass
            elif line.startswith("# "):
                pass
            elif line.startswith("## "):
                if text:
                    print(f"{chapter:02d}", " ".join(text), sep="\t", file=g)
                chapter += 1
                text = []
            else:
                text.append(line)

        print(f"{chapter:02d}", " ".join(text), sep="\t", file=g)
