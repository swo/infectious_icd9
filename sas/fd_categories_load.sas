* Written by R;
*  write.foreign(cats, "fd_categories_data.txt", "fd_categories_load.sas",  ;

DATA  fd_categories ;
LENGTH
 diagnosis_category $ 14
 diagnosis_category_desc $ 44
;

INFILE  "fd_categories_data.txt" 
     DSD 
     LRECL= 62 ;
INPUT
 diagnosis_category
 diagnosis_category_desc
 tier
;
RUN;
