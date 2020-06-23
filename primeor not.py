def finding_factors(number):
    count=0
    for i in range(2,(number//2+1)):
        if(number % i==0):
            count=count+1
            return count
        num=int(input('please enetr any number:'))
        cnt=finding_factors(num)
        if(cnt==0 and num!=1):
            print('%d is a prime number '%num)
        else:
            print('%d is not a prime number'%num)
