#!/bin/bash
cycle=true
while $cycle
do
    echo -n -e "\e[0;36mPlease input file extension (q to quit):\e[0;0m"
    read  ext
    if test $ext = "q"
    then
        break
    fi
    echo -n -e "\e[0;36mPlease input directory to search (q to quit):\e[0;0m"
    read dir
    if test $dir = "q"
    then
        break
    fi
    echo -n -e "\e[0;33m"
    find . -name "*.${ext}"
    var=`find . -name "*.${ext}" |wc -l`
    echo -e "\e[0;31m$var\e[0;35m file(s) found."
done

