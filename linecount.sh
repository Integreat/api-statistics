#!/bin/bash
LANGS="/en/ /de/ /ar/";
MONTHS="Jan Feb";
for MONTH in $MONTHS; do
    for LANG in $LANGS; do
        for i in 0{1..9} {10..31} ; do
            echo "$LANG; $i/$MONTH; $(cat access.log | grep "$i/$MONTH/2018" | grep $LANG | wc -l)";
        done;
    done;
done
