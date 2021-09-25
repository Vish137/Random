import numpy as np
def CES(L, K, gamma,*args):
    #CES parameterisation
    if gamma==0:
        raise ZeroDivisionError('gamma must be non-zero')
    #TFP
    A=10
    #Output elasticities
    if args:
        if len(args)!=1:
            raise ValueError('You need to indicate the value of output elasticity, a, only')
        a=args[0]
        b=1-a
    else:
        a=0.5
        b=1-a
    return A * (a*L**(gamma) + b*K**(gamma))**(1/gamma)

