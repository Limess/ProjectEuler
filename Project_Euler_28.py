def sum_diagonals_of_spiral(size):
    n = 1
    step = 2
    total = 0
    since_last = 0
    while n <= size**2: #size**2 appears on the last diagonal of that size
        total += n      #distance between each diagonal in each step
        n += step       #step size varies after 4 diagonals
        since_last +=1  #count of 4 diagonals in each step
        if since_last==4:
            step += 2
            since_last = 0
    return total

size = int(input("What size of spiral?" ))

print(sum_diagonals_of_spiral(size))
