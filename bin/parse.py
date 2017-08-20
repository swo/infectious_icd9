#!/usr/bin/env python3

import json, re

def expand_range(start, end):
    '''
    Expand a range into individual codes

    e.g., ('010', '015') -> ['010', '011', '012', '013', '014', '015']
    '''
    assert len(start) == len(end)
    w = len(start)
    return [str(i).rjust(w, '0') for i in range(int(start), int(end) + 1)]

def in_code(query, reference):
    '''Ask if the query code was present in the reference code (or range)'''

    # remove dots from reference
    reference = re.sub('\.', '', reference)

    # check if this was a range
    if '-' in reference:
        # recursively check for in_code on each part of the range
        start, end = reference.split('-')
        references = expand_range(start, end)
        return any([in_code(query, r) for r in references])
    else:
        # if not recursive, just ask if the query fits this code
        return query.startswith(reference)

def matching_code(query, references):
    '''
    Find the first reference that matches the query. If no matches, then return
    None.
    '''
    for ref in references:
        if in_code(query, ref):
            return ref

    return None

# read in the categories
with open('diagnosis_categories.json') as f:
    dxcat = json.load(f)

# first, output just the code names, tiers, etc.
with open('../fd_categories.tsv', 'w') as f:
    print('diagnosis_category', 'diagnosis_category_desc', 'tier', sep='\t', file=f)
    for cat in dxcat:
        print(cat['short'], cat['diagnosis'], cat['tier'], sep='\t', file=f)

# loop over each diagnostic code
with open('icd.tsv') as fin, open('../fd_codes.tsv', 'w') as fout:
    print('code', 'reference', 'diagnostic_category', sep='\t', file=fout)

    header = next(fin)
    for line in fin:
        query_code, desc = line.rstrip().split('\t')

        # for each query code, compare against each diagnostic category
        for ref in dxcat:
            if matching_code(query_code, ref['excludes']) is None:
                match = matching_code(query_code, ref['codes'])
                if match is not None:
                    print(query_code, match, ref['short'], sep='\t', file=fout)