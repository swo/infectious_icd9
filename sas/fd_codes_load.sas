* Written by R;
*  write.foreign(codes, "../fd_codes_data.txt", "../fd_codes_load.sas",  ;

DATA  fd_codes ;
LENGTH
 code $ 5
 diagnosis_category $ 14
;

INFILE  "../fd_codes_data.txt" 
     DSD 
     LRECL= 28 ;
INPUT
 code
 diagnosis_category $ 
;
RUN;
