def add_tip(total, tip_percent): 
    '''Return the total amount including tip''' 
    tip = tip_percent*total
    return total + tip
def mean(a,b,c):
    return (a+b+c)/3.
def hyp(leg1, leg2):
    return (leg1**2 + leg2**2)**0.5
def perimeter(base, height):
    return 2*base+2*height
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)
    
    


