#!/usr/bin/env python3

"""
converts the textpart-per-chap to textpart-per-sentence.
"""


input_filename = f"text/orat27.chap.txt"
output_filename = f"text/orat27.sent.txt"

with open(input_filename) as f, open(output_filename, "w") as g:
    for line in f:
        line = line.strip()
        ref, text = line.split(maxsplit=1)
        sentence = []
        sent_num = 1
        for token in text.split():
            sentence.append(token)
            if "." in token or ";" in token or "·" in token or "!" in token:
                print(f"{ref}.{sent_num:02d} {' '.join(sentence)}", file=g)
                sent_num += 1
                sentence = []
    assert sentence == [], f"finished para {ref} mid-sentence"
