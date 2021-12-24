import math

def module(a):
    if a<0:
        a = a * (-1)
    return a

error = 0.001
n = 1        
sum = -0.5
function_old = 0
function_new = 1 + sum
while True:               
    if (module(function_old-function_new) > error):        
        k = (-1)/(4*(n**2)+6*n+2)
        sum = k*sum
        function_old = function_new
        function_new += sum        
        n += 1
    
    elif (module(function_old-function_new) <= error):
        break

print('Значение фунции: ', function_new)
print('Значение косинуса, посчитанное через библиотеку MATH: ', math.cos(1))