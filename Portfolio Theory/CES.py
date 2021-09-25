import numpy as np
def CES(L, K, gamma,*args):
    #CES parameterisation
    if gamma==0:
        raise ZeroDivisionError('gamma must be non-zero')
    #Output elasticities
    if args:
        if len(args)!=2:
            raise ValueError('You need to indicate the value of total factor production and output elasticity, A and a, only')
        A=args[0]
        a=args[1]
        b=1-a
    else:
        A=10
        a=0.5
        b=1-a
    return A * (a*L**(gamma) + b*K**(gamma))**(1/gamma)

