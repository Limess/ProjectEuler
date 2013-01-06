def not_fail_method(max_a):
    a=3
    sum_r_max=0
    while a<=max_a:
        if a%2==0:
            sum_r_max+=a*(a-2)
        elif a%2!=0:
            sum_r_max+=a*(a-1)
        a+=1
    return sum_r_max

print("The answer is: ", not_fail_method(1000))
