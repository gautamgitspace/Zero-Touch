
#!/bin/bash
var=$(cat foo.txt | head -n 1)
for file in *.txt*; do
  echo -e "$var\n$(cat $file)" > $file
done
echo | cat f.txtaa | tail -n+2 > first_in_seq.txt
rm f.txtaa
