#!/bin/bash 
#sort --unique --output=ptermsSorted.txt pterms.txt
#sort --unique --output=rtermsSorted.txt rterms.txt
#sort --unique --output=scoresSorted.txt scores.txt

# there might be problems with the buffer/ stuff out of order. check

cat reviews.txt | perl break.pl | db_load -T -t hash rw.idx
sort --unique pterms.txt | perl break.pl | db_load -T -t btree pt.idx
sort --unique rterms.txt | perl break.pl | db_load -T -t btree rt.idx
sort --unique scores.txt | perl break.pl | db_load -T -t btree sc.idx


