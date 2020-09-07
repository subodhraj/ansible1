#!/bin/bash
echo "enter a string"
read a

d=`echo -n $a | wc -c`
#echo "d is $d"

i=$d
while [ $i -ge 1 ]
 do
  # echo " i is $i"
    
   f=`echo $a | cut -c $i`
  # echo "f is $f"
   g="$g""$f"
   #echo $g
   ((i--))
 done
echo $g
if [ "$a" = "$g" ]
 then 
  echo "it is palindrom"
 else
	 echo " it is not palindrome"
fi
exit
