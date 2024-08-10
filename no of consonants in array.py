my_array=['v','e','b','o']
count=0
for i in range(len(my_array)):
    if(my_array[i]!="a" and my_array[i]!="e" and my_array[i]!="i" and my_array[i]!="o" and my_array[i]!="u" and my_array[i]!="A" and my_array[i]!="E" and my_array[i]!="I" and my_array[i]!="O" and my_array[i]!="U"):
        count+=1
print("no.of.consonants:",count)        
