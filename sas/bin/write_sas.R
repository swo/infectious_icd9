#!/usr/bin/env Rscript

library(foreign)
library(readr)

cats = read_tsv('../../fd_categories.tsv')

codes = read_tsv('../../fd_codes.tsv') %>%
  left_join(cats, by='dx_cat')

write.foreign(codes, '../fd_codes_data.txt', '../fd_codes_load.sas', package='SAS', dataname='fd_codes')
