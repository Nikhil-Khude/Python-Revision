def check_prime(number):
    if number <=1:
        print(number,"is not prime")
    for i in renge(2,number):
        if number % 1==0:
            print(number,"is not prime ")
            return
    print(number,"is prime")