* Written by R;
*  write.foreign(codes, "../fd_codes_data.txt", "../fd_codes_load.sas",  ;

DATA  fd_codes ;
LENGTH
 code $ 5
 dx_cat $ 15
 desc $ 44
 t3_acute_respiratory $ 1
;

INFILE  "../fd_codes_data.txt" 
     DSD 
     LRECL= 74 ;
INPUT
 code
 dx_cat
 desc
 tier
 t3_acute_respiratory $ 
;
RUN;
