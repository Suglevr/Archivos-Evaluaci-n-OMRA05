num_vlan =  int(input("Favor ingresar el número de vlan: "))
if 1 <= num_vlan <= 1000:
    print("Rango Normal")
    
elif 1000 <= num_vlan <= 4049:
    print("Rango Extendido")

else: 
    print("Rango no Valido")




