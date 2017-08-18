#!/usr/bin/env python3

import json

# read in the categories
with open('diagnostic_categories.json') as f:
    dxcat = json.load(f)

print('short', 'diagnosis', 'tier', sep='\t')
for cat in dxcat:
    print(cat['short'], cat['diagnosis'], cat['tier'], sep='\t')
