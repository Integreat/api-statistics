#!/bin/bash
# Param1: log file, Param2: city name

if [ -z "$LANGS" ]; then
    LANGS="/en/ /de/ /ar/ /fr/ /es/ /fa/ /am/ /ru/";
fi
echo "$MONTHS"
if [ -z "$MONTHS" ]; then
    MONTHS="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec";
fi

if [[ -z $1 || $1 == "--help" || $1 == "-h" ]]; then
	echo "Usage: linecount.sh [ACCESS.LOG] [CITY]"
	echo ""
	echo "You can set environment variables LANGS or MONTHS."
	echo "Default values:"
	echo "LANGS=$LANGS"
	echo "MONTHS=$MONTHS"
	exit
fi

for MONTH in $MONTHS; do
    for LANG in $LANGS; do
        for i in 0{1..9} {10..31} ; do
            echo "$LANG; $i/$MONTH; $(cat $1 | grep "$i/$MONTH/2018" | grep $LANG | grep $2 | grep "modified_content/pages" | wc -l)";
        done;
    done;
done
