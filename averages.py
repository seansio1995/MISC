def median(a,b,c):
    if (a<=b and a>=c) or (a<=c and a>=b):
        return a
    if (b<=c and b>=a) or (b<=a and b>=c):
        return b
    if (c<=b and c>=a) or (c<=a and c>=b):
        return c


def middle_average(a,b,c):
    mean_value=mean(a,b,c)
    median_value=median(a,b,c)
    rms_value=rms(a,b,c)
    return median(mean_value,median_value,rms_value)

    
print(median(1,3,5))
