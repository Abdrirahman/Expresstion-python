# The formula of displacement is = (v2 - u2)/ (2a)
u = float(input("Enter the initial speed")) # u = initial
v = float(input("Enter the final speed"))  # v = final
a = float(input("Enter the acceleration")) # a = acceleration

displacement = (v**2 - u**2) / (2 * a)
print("Displacement is ", displacement)