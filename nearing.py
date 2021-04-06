#nearing mechanics, p 27 o 32

def quad_eq_sol_iterative(a,b,c,N) :
    x1=x1_0=-c/b
    x2=x2_0=-b/a
    for i in range(N) :
        x1=x1_0-(a*x1**2)/b
        x2=x2_0-c/(a*x2**2)
    return x1,x2
print("\n")
print(quad_eq_sol_iterative(0.001,1000,0.001,20))
