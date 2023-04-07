#!/bin/bash

#LINES=$(cat pdfs.txt)

cat pdfs.txt | while read line
do
   num=$(echo "$line" | awk '{print $1}')
   url=$(echo "$line" | awk '{print $2}')
   name=$(echo "$url" | sed 's/^.*notes\/\(.*\.pdf\)$/\1/')
   wget "$url"
   noext="${name%.*}"
   mv "$name" "$num-$noext.pdf"
done

#for LINE in $LINES; do
#   echo "$LINE"
#   echo
#done
