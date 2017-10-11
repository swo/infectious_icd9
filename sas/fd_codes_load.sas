* Written by R;
*  write.foreign(codes, "../fd_codes_data.txt", "../fd_codes_load.sas",  ;

DATA  fd_codes ;
LENGTH
 code $ 5
 diagnosis_category $ 14
 t3_acute_respiratory $ 1
;

INFILE  "../fd_codes_data.txt" 
     DSD 
     LRECL= 32 ;
INPUT
 code
 diagnosis_category
 t3_acute_respiratory $ 
;
RUN;
