#!/usr/bin/env Rscript

library(foreign)
library(readr)

cats = read_tsv('../../fd_categories.tsv')
write.foreign(cats, '../fd_categories_data.txt', '../fd_categories_load.sas', package='SAS', dataname='fd_categories')

codes = read_tsv('../../fd_codes.tsv')
write.foreign(codes, '../fd_codes_data.txt', '../fd_codes_load.sas', package='SAS', dataname='fd_codes')
