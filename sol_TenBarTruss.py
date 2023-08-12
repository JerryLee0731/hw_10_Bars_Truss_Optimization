import math
import numpy

class TenBarTruss:
    
    def __init__(self, elements):
        
        K = numpy.zeros((12,12))
      
        for i in range(10):
            a = elements[i].nodei.node_id*2-1
            b = elements[i].nodej.node_id*2-1
        
            k_temp  = elements[i].K_each
            K[a-1:a+1, a-1:a+1] = K[a-1:a+1, a-1:a+1]+ k_temp[0:2, 0:2]
            K[a-1:a+1, b-1:b+1] = K[a-1:a+1, b-1:b+1]+ k_temp[0:2, 2:4]
            K[b-1:b+1, a-1:a+1] = K[b-1:b+1, a-1:a+1]+ k_temp[2:4, 0:2]
            K[b-1:b+1, b-1:b+1] = K[b-1:b+1, b-1:b+1]+ k_temp[2:4, 2:4]

        print("K=", K)
        
        self.K = K


        f = numpy.zeros(12)
        f[3] = 10**7
        f[7] = 10**7

        q = numpy.zeros(12)

        K_reduced = K[:8, :8]
        f_reduced = f[:8]
        K_reduced_inv = numpy.linalg.inv(K_reduced)
        q_reduced = numpy.dot(K_reduced_inv, f_reduced)
        q[:8] = q_reduced
        print("q= ", q)

        self.q = q


        sigma = numpy.zeros(12)
        for i in range(10):
            a = elements[i].nodei.node_id*2-1
            b = elements[i].nodej.node_id*2-1
            
            A = [-elements[i].cos, -elements[i].sin, elements[i].cos, elements[i].sin]
            q_element = [q[a-1], q[a], q[b-1], q[b]]
            sigma[i] = elements[i].E/elements[i].L*numpy.dot(A, q_element)

        print("sigma= ", sigma)
        self.sigma = sigma


        K_reaction = K[8:12, :]
        R = numpy.dot(K_reaction, q.T)
        print("R=", R)
        
        self.R = R


        total_mass = 0
        for i in range(10):
            total_mass = total_mass + elements[i].mass

        print("total_mass= ", total_mass)

        self.total_mass = total_mass


