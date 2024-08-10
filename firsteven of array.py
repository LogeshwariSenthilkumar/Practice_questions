my_array=[1,3,7,5,6]
count=0
for i in range(len(my_array)):
    if(my_array[i]%2==0):
        print("First even number is:",my_array[i])
        count=+1
        if(count==1):
            break;
