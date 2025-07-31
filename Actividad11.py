propietarios={}
vehiculos={}
si=0
no=0
numero_propietarios= int(input("Ingrese cantidad de propietarias a ingresar:"))
for i in range(numero_propietarios):
    print(f"---Propietario {i+1}---")
    nit=input("Ingrese número de nit")
    nombre_completo=input("Ingrese nombre completo de propietario:")
    telefono=input("Ingrese telefono de contacto:")
    cantidad_vehivulos=int(input("Ingrese cantidad de vehiculos:"))
    for vehiculo in range(cantidad_vehivulos):
        print(f"---DATOS DE VEHICULO {vehiculo +1}")
        placa= input("Ingrese placa de vehiculo:")
        marca= input("Ingrese marca de vehiculo:")
        modelo= input("Ingrese modelo de vehiculo")
        year= int(input("Ingrese año de vehiculo:"))
        impuesto= input("¿Tiene impuesto? Si/No:")
        if impuesto =="si":
            si += 1
        elif impuesto =="no":
            no+=1

    propietarios[nit]={
        "nombre":nombre_completo,
        "telefono":telefono,
        "vehiculos":{
                "placa":placa,
                "marca":marca,
                "modelo":modelo,
                "año":year,
                "impuesto":impuesto

            }
    }

for propietarios,propietario in propietarios.items():
    print("---DATOS DE PROPIETARIOS---")
    print("---"*4)
    print(f"Nombre:{propietario["nombre"]}")
    print(f"Telefono:{propietario["telefono"]}")
    print("---VEHICULOS---")
    print(f"Placa:{propietario["vehiculos"]["placa"]}")
    print(f"Marca:{propietario["vehiculos"]["marca"]}")
    print(f"Modelo:{propietario["vehiculos"]["modelo"]}")
    print(f"Año:{propietario["vehiculos"]["año"]}")
    print(f"Impuesto:{propietario["vehiculos"]["impuesto"]}")
    print("---"*4)

buscar_propietario= input("Ingrese número de identificación para buscar propietario:")
if buscar_propietario in propietarios:
    propi= propietarios[buscar_propietario]
    print("---Propietario---")
    print(f"Nombre:{propi["Nombre"]}")
    print(f"Telefono:{propi["telefono"]}")
    print("---VEHICULOS---")
    print(f"Marca:{propi["vehiculos"]["placa"]}")
    print(f"Modelo:{propi["vehiculos"]["modelo"]}")
    print(f"Año:{propi["vehiculos"]["año"]}")
    print(f"Impuesto:{propi["vehiculos"]["impuesto"]}")

print("---CANTIDAD DE CARROS CON IMPUESTO---")
print(f"Cantidad de carros que tienen impuesto:{si}\nCantidad de carros que no tienen impuestos:{no}")