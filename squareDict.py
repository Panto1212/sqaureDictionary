print("How many keys do you want in your dictionary?")
n = int(input())

square = {}
for x in range(n) :
    print("Integer:")
    key = int(input())
    value= int(key)*int(key) 
    square[key]= value
   
print(square)