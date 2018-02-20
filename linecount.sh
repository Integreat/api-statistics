#!/bin/bash
# Param1: log file, Param2: city name
LANGS="/en/ /de/ /ar/";
MONTHS="Jan Feb";
for MONTH in $MONTHS; do
    for LANG in $LANGS; do
        for i in 0{1..9} {10..31} ; do
            echo "$LANG; $i/$MONTH; $(cat $1 | grep "$i/$MONTH/2018" | grep $LANG | grep $2 | grep "modified_content/pages" | wc -l)";
        done;
    done;
done
