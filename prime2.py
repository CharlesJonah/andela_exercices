
def prime_num(number):
    output = []
    
    for num in range(2, number+1):
        prime = True
        for i in range(2, num):

            
            if(num % i == 0):
                prime = False
        if prime:
            
            output.append(num)

    return output

print(prime_num(100))