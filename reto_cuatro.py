
import json
from pprint import pprint

winners = ("P" "G" "S" "X" "T" "Y" "F" "E" "H")
biblioteca = {"M": 31, "F": 32, "P": 55, "E": 40, "N": 50, "Z": 84, "G": 74, "X": 56, "R": 99, "H": 88}
sorted(biblioteca.items(),key=lambda item:item[1])
list1 = []
list2 = []
list3 = []
list4 = []
var1 = 0

for b in biblioteca:
  list1.append(b)
  list2.append(biblioteca[b])

for it in winners:
  if it in list1:
    list3.append(it)
  else:
    " " 

for w in list3:
  list4.append(biblioteca[w])

for num in list4:
  var1 = var1 + num

print("output=",end="")
print(var1, '\n')

for its in list3:
  print(its, end=" ")