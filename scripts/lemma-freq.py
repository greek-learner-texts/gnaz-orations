#!/usr/bin/env python

lemma_freqs_dict = dict()
freq_stats_dict = dict()

input_filename = "analysis/orat27.sent.lemma.txt"
output_filename = "analysis/orat27.freq.lemma.txt"

with open(input_filename, 'r') as f:
    for line in f:
        if ".lemma" in line:
            for lemma in line.split()[1:]:
                if lemma_freqs_dict.get(lemma) is None:
                    lemma_freqs_dict[lemma] = 0
                lemma_freqs_dict[lemma] += 1

lemma_freqs = reversed(sorted(lemma_freqs_dict.items(), key=lambda lf: lf[1]))

with open(output_filename, 'w') as g:
    for [lemma, freq] in lemma_freqs:
        if freq_stats_dict.get(freq) is None:
            freq_stats_dict[freq] = 0
        freq_stats_dict[freq] += 1
        print(f'{freq}\t{lemma}', file=g)

freq_stats = reversed(sorted(freq_stats_dict.items(), key=lambda fs: fs[1]))

print('Lemma frequencies:')
for [freq, count] in freq_stats:
    print(f'{freq} occurrence(s): {count} lemma(s)')
