masa=float(input("ingrese datos"))
altura=float(input("ingrese datos"))

imc=masa/altura**2

print("tu imc es:"+str(imc))
if imc >25 :
 print("tienes sobrepeso")