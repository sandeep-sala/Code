try:    
    factors_finding = lambda n : [str(1)] + [ str(i) for i in range(2,n+1) if n%i==0 ]
    factors = factors_finding(int(input()))
    print(  len(factors)  )
    print( " ".join(factors) )
except Exception as e:
    print(e)
