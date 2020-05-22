#Minimum Unique Array Sum Challenge

def processInput ( input ):
    n = len(input)
    sum = input[0]
    prev = input[0]
    
    for i in range (1, n):
      if input[i] <= prev:
        prev = prev + 1
        sum = sum + prev
      else:
        sum = sum  + input[i]
        prev = input[i]
        
    return sum

print (processInput([24, 76, 44, 23, 44, 67, 235]))

#649