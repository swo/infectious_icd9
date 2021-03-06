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

def matching_category(query_code, categories, no_match_category):
    '''Find the first category that matches the query. If no matches, return None'''
    for cat in categories:
        if matching_code(query_code, cat['excludes']) is None:
            match = matching_code(query_code, cat['codes'])
            if match is not None:
                out = dict(cat)
                out['matched_reference'] = match
                return out

    return no_match_category

# read in the categories
with open('diagnosis_categories.json') as f:
    dxcat = json.load(f)

# first, output just the code names, tiers, etc.
with open('../fd_categories.tsv', 'w') as f:
    print('dx_cat', 'desc', 'tier', 't3_acute_respiratory', sep='\t', file=f)
    for cat in dxcat:
        print(cat['short'], cat['diagnosis'], cat['tier'], cat['t3_acute_respiratory'], sep='\t', file=f)

# the last category is "all remaining codes", so look at that separately
no_match_cat = dxcat.pop()

# loop over each diagnostic code
with open('icd.tsv') as fin, open('../fd_codes.tsv', 'w') as fout:
    print('code', 'dx_cat', sep='\t', file=fout)

    header = next(fin)
    for line in fin:
        query_code, desc = line.rstrip().split('\t')

        cat = matching_category(query_code, dxcat, no_match_cat)
        print(query_code, cat['short'], sep='\t', file=fout)
