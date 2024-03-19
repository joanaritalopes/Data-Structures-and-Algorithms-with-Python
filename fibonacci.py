# Recursive implemetation
def fibonacci(n):
  # base cases
  if n == 1:
    return n
  elif n == 0:
    return n
  
  else: 
    # recursive step
    print("Recursive call with {0} as input".format(n))
    return fibonacci(n - 1) + fibonacci(n - 2)


#Interactive implementation
def fibonacci(n):
    fib_list = [0,1]
    if n <= len(fib_list) - 1:
        return fib_list[n]
    else:
        while n > 1:
            next_fib = fib_list[-1] + fib_list[-2]
            fib_list.append(next_fib)
            n -=1
    return fib_list[-1]