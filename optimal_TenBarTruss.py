import math
from scipy.optimize import minimize

from construct_TenBarTruss import construct_elements
from sol_TenBarTruss import TenBarTruss

def main(r):
    
    elements = construct_elements(r[0], r[1])
    tenBarTruss = TenBarTruss(elements)
    
    return tenBarTruss


def func(r):
    
    tenBarTruss = main(r)
    
    return tenBarTruss.total_mass


sigmaY = 250*10**6


def constraint_sigma1(r):

    tenBarTruss = main(r)

    return sigmaY-tenBarTruss.sigma[0]


def constraint_sigma2(r):

    tenBarTruss = main(r)
    
    return sigmaY-tenBarTruss.sigma[1]
"""
def constraint_sigma3(r):

    tenBarTruss = main(r)
    
    return sigmaY-tenBarTruss.sigma[2]

def constraint_sigma4(r):

    tenBarTruss = main(r)
    
    return sigmaY-tenBarTruss.sigma[3]

def constraint_sigma5(r):

    tenBarTruss = main(r)
    
    return sigmaY-tenBarTruss.sigma[4]

def constraint_sigma6(r):

    tenBarTruss = main(r)
    
    return sigmaY-tenBarTruss.sigma[5]
"""


def constraint_q2(r):

    tenBarTruss = main(r)
    q2_x = tenBarTruss.q[2]
    q2_y = tenBarTruss.q[3]
    s2 = math.sqrt(q2_x**2+q2_y**2)

    return 0.02-s2


constraint1 = {'type': 'ineq', 'fun': constraint_sigma1}
constraint2 = {'type': 'ineq', 'fun': constraint_sigma2}
"""
constraint3 = {'type': 'ineq', 'fun': constraint_sigma3}
constraint4 = {'type': 'ineq', 'fun': constraint_sigma4}
constraint5 = {'type': 'ineq', 'fun': constraint_sigma5}
constraint6 = {'type': 'ineq', 'fun': constraint_sigma6}
"""
constraint0 = {'type': 'ineq', 'fun': constraint_q2}

constraints = [constraint1, constraint2, constraint0]
#constraints = [constraint1, constraint2, constraint3, constraint4, constraint5, constraint6, constraint0]

initial_guess = [0.4, 0.3]

r1boundary = [0.001, 0.5]
r2boundary = [0.001, 0.5]
boundaries = (r1boundary, r2boundary)

result = minimize(fun=func, x0=initial_guess, bounds=boundaries, constraints=constraints)
print(result.x)
