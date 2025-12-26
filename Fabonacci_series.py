def fabonacci_series(n):
    if(n==1):
        return 1
    if(n==0):
      return 0
    return fabonacci_series(n-1)+fabonacci_series(n-2)
    

result =fabonacci_series(5)
print(result)