productos= {}

numeros_productos= int(input("Ingrese cantidad de productos a ingresar:"))

mujer=0
hombre=0
niño=0

for i in range(numeros_productos):
    print(f"---Producto no.{i +1}")
    while True:
        codigo= input("Ingrese codigo de producto:")
        if codigo in productos:
            print("Codigo repetido....No valido")
        else:
            break
    nombre= input("Ingrese nombre de producto:").lower()
    categoria= input("Ingrese categoria (Hombre, Mujer, Niño):").lower()
    if categoria == "mujer":
        mujer +=1
    elif categoria == "niño":
        niño +=1
    elif categoria == "hombre":
        hombre += 1
    else:
        print("Categoria no valida...")

    talla= input("Ingrese talla (S,M,L,XL) :").lower()
    while True:
        precio_unitario= float(input("Ingrese precio:"))
        if precio_unitario <= 0:
            print("Precio no valido...Debe ser mayor a 0")
        else:
            break
    stock= int(input("Ingrese cantidad de stock de producto:"))
    if stock < 0:
        print("Stock no puede ser negativo....")

    productos[codigo]= {
        "nombre":nombre,
        "categoria": categoria,
        "talla":talla,
        "precio_unitario": precio_unitario,
        "stock":stock,
    }
print(f"---LISTA DE PRODUCTOS---")
for codigo,dato in productos.items():
    print("---"*4)
    print(f"Nombre de producto:{dato["nombre"]}")
    print(f"Categoria de producto:{dato["categoria"]}")
    print(f"talla:{dato["talla"]}")
    print(f"Precio de producto:{dato["precio_unitario"]}")
    print(f"Stock de producto:{dato["stock"]}")
    print("---"*4)

print("---BUSQUEDA DE PRODUCTOS---")
codigo_solicitato= input("Ingrese codigo de producto a buscar:")
if codigo_solicitato in productos:
    product=productos[codigo_solicitato]
    print("---DETALLES DEL PRODUCTO---")
    print(f"Nombre producto:{product["nombre"]}")
    print(f"Categoria:{product["categoria"]}")
    print(f"Talla:{product["talla"]}")
    print(f"Precio:{product["precio_unitario"]}")
    print(f"stock:{product["stock"]}")
else:
    print("Producto no encontrado....")

print("---VALOR TOTAL DE PRODUCTOS---")
for codigo, valor in productos.items():
    precio= valor["precio_unitario"] * valor["stock"]
    print(f"El valor total de inventario de  -{valor["nombre"]}- es {precio}")

print("---PRODUCTO POR CATEGORIA---")
print(f"Hay {mujer} productos en categoria de -Mujer-")
print(f"Hay {hombre} productos en categoria de -Hombre-")
print(f"Hay {niño} productos en categoria de -Niño-")

