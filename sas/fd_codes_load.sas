* Written by R;
*  write.foreign(codes, "fd_codes_data.txt", "fd_codes_load.sas",  ;

DATA  fd_codes ;
LENGTH
 code $ 5
 reference $ 11
 diagnosis_category $ 14
;

INFILE  "fd_codes_data.txt" 
     DSD 
     LRECL= 38 ;
INPUT
 code
 reference
 diagnosis_category $ 
;
RUN;
