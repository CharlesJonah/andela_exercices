
#Code written in Python 3
def prime_num(number):
    output = []
    #Loop to get number n to use for testing
    if isinstance(number,int):
        if number > 1:
            for num in range(2, number+1):
                prime = True
                for i in range(2, num):

                    #If the modulus of num and i is zero the disqulaify the number from being a prime
                    if(num % i == 0):
                        prime = False
                if prime:
                    #append the results to a list
                    output.append(num)

            return output
        else:
            print("Enter number greater than 1.")


    else:
        print("Only numbers allowed.")

print(prime_num('30'))

