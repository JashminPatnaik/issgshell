%%bash

curl -s -o NAVAll.txt https://www.amfiindia.com/spages/NAVAll.txt

awk -F';' 'NR>1 && NF>=5 {print $4"\t"$5}' NAVAll.txt > scheme_nav.tsv

echo "First 10 lines of scheme_nav.tsv:"
head scheme_nav.tsv
