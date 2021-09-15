# Gregory of Nazianzus Orations

{{ describe what is being done, the process being followed, and who is involved in the work }}

This text is being prepared as part of the [Greek Learner Texts Project](https://greek-learner-texts.org/).

## Contributors

* James Tauber (initial setup, corrections)
* Seumas Macdonald (corrections, lemma overrides)

## Source

Original text from [Open Greek and Latin's First1KGreek Project](https://github.com/OpenGreekAndLatin/First1KGreek).

## Progress

Main text in XML has been corrected, extracted, segmented into sentences, and normalized. It is currently being lemmatized.

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

## Pipeline

With Pipfile loaded,

* `scripts/extract_ogl.py > text/orat27.txt`
* `scripts/text-to-chap.py`
* `scripts/chap-to-sent.py`
* `scripts/add-norm.py`
* `scripts/lemmatise.py` (using `manual-data/lemma-overrides.yaml`)
