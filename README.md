# Infectious disease ICD9-CM codes

Codes from eTable 2 in Fleming-Dutra *et al*., *JAMA* (2016)
doi:[10.1001/jama.2016.4151](http://dx.doi.org/10.1001/jama.2016.4151).

*Caveat*: The Table stipulates that visits should not be categorized as
"Bronchitis, bronchiolitis" if "the 2nd or 3rd diagnosis was chronic bronchitis
(491), emphysema (492), or COPD (496)."

## Files

`fleming_dutra_codes.tsv` has one record per diagnosis code:

- *code* is the diagnosis code
- *code_diagnosis* is the description of the code
- *category_short* is an abbreviation of the diagnosis category
- *tier* is the "tier" of the diagnosis category
- *category* is the long name of the diagnosis category
- *reference* is the code or range given in the Table that justify the refers to this code

`diagnostic_categories.tsv` is a supplement that has has information about
the names of diagnosis categories, a short name handy for coding, and the
"tier" of the diagnosis. This is redundant with the previous file.

`bin/diagnostic_categories.json` has the information from the Table, but in a parseable format.

`bin/icd.tsv` is a list of all ICD9 codes.

`bin/interpret.py` is a little script to spit out the small tsv.

`bin/link.py` is the script to spit out a big tsv. I linked the small tsv and
the big one to make the main data file.

`sas/` has a `sas7bdat` version of the main data file as well as two text
files, one of which has the data in a csv format, and the other that has SAS
commands for reading in that csv.
