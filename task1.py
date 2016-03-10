# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:29:08 2016

@author: Edric
"""

import numpy as np


 #function of lu that perform finding  
def lu(A, b):
    
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i,k] != 0.0:
                lam = A[i,k] / A[k,k]
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                A[i, k] = lam
    
    for k in range(1,n):
        b[k] = b[k] - np.dot(A[k,0:k], b[0:k])
    b[n-1]=b[n-1]/A[n-1, n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n]))/A[k,k]

    return list(b)
    
#function of sor that perform finding
def sor(A, b):
    
    Diag = np.diag(np.diag(A))
    Ltmatrix = np.tril(-A,-1)
    Utmatrix = A-Ltmatrix-Diag
   
   
    spars = max(abs(np.linalg.eigvals(np.dot(np.linalg.inv(Diag),(Ltmatrix+Utmatrix)))))

    w_omega = 2*(1 - np.sqrt(1 - ((spars)**2)))/((spars)**2)
    x = np.zeros_like(b)
    for itr in range(10):
        for i in range(len(b)):
            sums = np.dot( A[i,:], x )
            x[i-1] = x[i-1] + w_omega*(b[i-1]-sums)/A[i-1,i-1]
        
    return list(np.array([x[1],x[2],x[3]]))

#function to solve using sor or lu depend on condition
def solve(A, b):
    
    if (np.all(A-A.T== 0) & np.all(np.linalg.eigvals(A)) > 0):
         print('Solve by sor(A,b)')
         return sor(A,b)
    else:
       
        print('Solve by lu(A,b)')
        return lu(A,b)

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = np.array([[2.0,1.0,6.0], [8.0,3.0,2.0], [1.0,5.0,1.0]])
    b = np.array([9.0, 13.0, 7.0])
    
    print(solve(A,b))
    
    A = np.array([[6566, -5202, -4040, -5224, 1420, 6229],
                 [4104, 7449, -2518, -4588,-8841, 4040],
                [5266,-4008,6803, -4702, 1240, 5060],
                [-9306, 7213,5723, 7961, -1981,-8834],
                [-3782, 3840, 2464, -8389, 9781,-3334],
                  [-6903, 5610, 4306, 5548, -1380, 3539.]]).astype(float)
    b = np.array([ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]).astype(float)
   # sol = solve(A,b)
    
