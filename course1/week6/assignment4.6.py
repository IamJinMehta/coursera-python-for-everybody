def computepay(h,r):
    if(h>40):
        h=h-40
        x=h*r*1.5
        y=40*r
        z=x+y
    else:
        z=h*r
    return z

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)
