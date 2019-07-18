#!/bin/bash

echo $1 $2 $3

if [ -z $2 ];
then
    PREFIX=http://
else
    PREFIX=$2
fi

if [ -z $3 ];
then
    API=/status
else
    API=$3
fi

if [ -s $1 ];
then
    mkdir -p ./output/bash

    echo "" > ./output/bash/response.txt
    while read LINE
    do
        URL=${PREFIX}${LINE}${API}
        echo $URL
        curl $URL >> ./output/bash/response.txt && echo "\n" >> ./output/bash/response.txt
    done < $1

    cat ./output/bash/response.txt | tr -d "{" | tr -d "}" | tr -d "\"" | awk -F':' '{ print $1 " " $2 " " $3 " " $4 " " $5 " " $6}' | \
        awk -F',' '{ print $1 " " $2 " " $3 " " $4 " " $5 " " $6 " " $7}' | awk -F' ' '{ print $2 "_" $4 " \t" $8 " \t" $10 }' > \
        ./output/bash/success_rate.txt
    tail -n +2 ./output/bash/success_rate.txt > ./output/bash/success_rate.txt2 && mv ./output/bash/success_rate.txt2 ./output/bash/success_rate.txt

    cat ./output/bash/success_rate.txt |awk '{print $1}' | sort | uniq  > ./output/bash/uniq.txt
    
    echo "" > ./output/bash/grouped.txt
    while read p; do
        app=$(echo $p | awk -F'_' '{print $1}')
        version=$(echo $p | awk -F'_' '{print $2}')
        rc=$(grep $p ./output/bash/success_rate.txt | awk '{print $2}' | paste -sd+ | bc)
        sc=$(grep $p ./output/bash/success_rate.txt | awk '{print $3}' | paste -sd+ | bc)
        
        echo "$app  $version    $rc     $sc" >> ./output/bash/grouped.txt
    done <./output/bash/uniq.txt
    tail -n +2 ./output/bash/grouped.txt > ./output/bash/grouped.txt2 && mv ./output/bash/grouped.txt2 ./output/bash/grouped.txt

    cat ./output/bash/grouped.txt | awk '{print $1 " " $2 " " $4/$3 }' > ./output/bash/agg.txt
    cat ./output/bash/agg.txt | awk '{ print "Applicaiton: " $1 "; Version: " $2 "; Success Rate: " $3 }'
else
    echo "File name required"
fi