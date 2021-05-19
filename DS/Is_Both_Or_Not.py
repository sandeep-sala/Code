try:
    is_both_or_not = lambda x : ("BOTH" if (x%5==0 and x%11==0) else "ONE" ) if (x%5==0 or x%11==0)  else "NONE"
    print(  is_both_or_not(int(input()))  )
except Exception as e:
    print(e)
