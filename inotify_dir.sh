#!/bin/bash
#filename: inotify_dir.sh
#

if [ "$#" -ne 1 ]; then
    echo "Usage: `basename $0` directoryName"
    exit 1
fi    

firstTime=0
lastFile=last.txt
recentFile=recent.txt
currentDir=$1

if [ ! -e "$lastFile" ]; then
    firstTime=1
fi    

shopt -s extglob
cd $currentDir && du -bs !($lastFile|$recentFile) > recent.txt 2> /dev/null

if [ "$firstTime" -ne 1 ]; then
    changes=$(sed '1,/@@/d' <(diff -Naur recent.txt last.txt))
    if [ -n "$changes" ]; then
        echo "Change:"
        echo "$changes" | tee $$.tmp
        echo

        filename=$(awk '/^+/||/^-/{print $2}' $$.tmp | sort -u)
        count=0
        for f in $filename; do
            echo "changed filename: $f"
            let "count+=1"
        done
        echo -e "\nA total of $count filenames were changed."
    else
        echo "The Directory has no changes.."
    fi
else
    echo "[First run] Archiving.."
fi


cp $recentFile $lastFile

rm -rf $$.tmp 2> /dev/null
