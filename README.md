# Infectious disease ICD9-CM codes

Codes from eTable 2 in Fleming-Dutra *et al*., *JAMA* (2016)
doi:[10.1001/jama.2016.4151](http://dx.doi.org/10.1001/jama.2016.4151).

*Caveat*: The Table stipulates that visits should not be categorized as
"Bronchitis, bronchiolitis" if "the 2nd or 3rd diagnosis was chronic bronchitis
(491), emphysema (492), or COPD (496)."

## Files

`fd_codes.tsv` has one record per diagnosis code:

- *code* is the diagnosis code
- *reference* is the code or range given in the Table that justify the refers to this code
- *diagnosis_category* is the abbreviation for the diagnosis category

`fd_categories.tsv` has one record per diagnosis category:

- *diagnosis_category* is the same as in `fd_codes.tsv`
- *diagnosis_category_desc* is the long name for the category, as per the Table
- *tier* is the "tier" of the diagnosis category, as per the Table

`bin/diagnostic_categories.json` has the information from the Table, but in a
machine-readable format.

`bin/icd.tsv` is a list of all ICD9 codes.

`bin/parse.py` is a little script to spit out the two data files.

`sas/` has a `sas7bdat` version of the main data file as well as two text
files, one of which has the data in a csv format, and the other that has SAS
commands for reading in that csv.
