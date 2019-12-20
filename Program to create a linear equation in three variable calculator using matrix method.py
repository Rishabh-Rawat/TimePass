import numpy as np

print("Format of Linear equations in three vaiables : ax+by+cz=d")
print("where, a,b,c are coefficients | x,y,z are variables | d is constant")
print("Please enter the values in accordance with this format")

E1=eval(input("Enter the coefficients of first equation in the form of a tuple "))
E2=eval(input("Enter the coefficients of second equation in the form of a tuple "))
E3=eval(input("Enter the coefficients of third equation in the form of a tuple "))
E4=eval(input("Enter the constants of three equations in the form of a tuple "))
x1,y1,z1=E1
x2,y2,z2=E2
x3,y3,z3=E3
c1,c2,c3=E4

coefficients_matrix=np.array([[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]])
constants_matrix=np.array([[c1],[c2],[c3]])

if round(np.linalg.det(coefficients_matrix))==0:
    print("No solution or Infintely many solutions")
else:
    inverse_of_coefficients_matrix=np.linalg.inv(coefficients_matrix)
    resultant_matrix=np.dot(inverse_of_coefficients_matrix,constants_matrix)
    print("x=",round(resultant_matrix[0][0]))
    print("y=",round(resultant_matrix[1][0]))
    print("z=",round(resultant_matrix[2][0]))
