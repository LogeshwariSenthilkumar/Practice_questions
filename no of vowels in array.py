my_array=['a','e','b','o']
count=0
for i in range(len(my_array)):
    if(my_array[i]=="a" or my_array[i]=="e" or my_array[i]=="i" or my_array[i]=="o" or my_array[i]=="u" or my_array[i]=="A" or my_array[i]=="E" or my_array[i]=="I" or my_array[i]=="O" or my_array[i]=="U"):
        count+=1
print("no.of.vowels:",count)        
