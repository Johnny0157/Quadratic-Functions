from math import sqrt
from math import pow

a = float(input("Enter LC: ")) # gather user inputs
b = float(input("Enter \"x\" Term coefficient: "))
c = float(input("Enter constant: "))

quad_fn = [a,b,c] # assign to a list

disc = pow(quad_fn[1],2) - 4*quad_fn[0]*quad_fn[2]

solns = []

# identify greater root

if disc >= 0: # if solution is an element of Real Numbers
    soln_1 = (-1*quad_fn[1] + sqrt(disc))/(2*quad_fn[0])
    soln_1 = str(soln_1)
    solns.append(soln_1)

else: # if solution has an imaginary component
    real = -1*quad_fn[1]/(2*quad_fn[0])
    imaginary = sqrt(-1*disc)/(2*quad_fn[0])
    soln_1 = str(real) + " + " + str(imaginary) + "i"
    solns.append(soln_1)

# identify lesser root

if disc >= 0: # if solution is an element of Real Numbers
    soln_2 = (-1*quad_fn[1] - sqrt(disc))/(2*quad_fn[0])
    soln_2 = str(soln_2)

else: # if solution has an imaginary component
    real = -1*quad_fn[1]/(2*quad_fn[0])
    imaginary = sqrt(-1*disc)/(2*quad_fn[0])
    soln_2 = str(real) + " - " + str(imaginary) + "i"

if soln_1 != soln_2:
    solns.append(soln_2)

print(f"The solutions to your function are: {solns}")