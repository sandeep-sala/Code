def fizzbuzz(n):
    replace = lambda x: "FizzBuzz" if x%3==0 and x%5==0 else "Fizz" if x%3 == 0 else "Buzz" if x%5==0 else x
    return [ replace(i) for i in range(1,n+1) ]


"""
def fizzbuzz(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]
    
"""



expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']
print(fizzbuzz(10), expected)