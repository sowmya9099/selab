
import math
def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None 
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
a = -0.05  
b = 1.2    
c = 20     
T_target = 25  
roots = quadratic_solver(a, b, c - T_target)
if roots is None:
    print("No real solution: temperature does not reach the target.")
else:
    print(f"Time(s) when temperature reaches {T_target}°C: {roots}")
