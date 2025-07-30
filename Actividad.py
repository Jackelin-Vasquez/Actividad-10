productos= {}

numeros_productos= int(input("Ingrese cantidad de productos a ingresar:"))

mujer=0
hombre=0
niño=0

for  producto in range(numeros_productos):
    print(f"---Producto no.{producto +1}")
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
    if categoria == "Niño":
        niño +=1
    if categoria == "hombre":
        hombre += 1

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
        "precio_Unitario": precio_unitario,
        "stock":stock,
    }

for codigo,dato in productos.items():
        print(f"---LISTA DE PRODUCTOS---\n---Producto---")
        print(f"Nombre de producto:{dato["nombre"]}:")
        print(f"Categoria de producto:{dato["categoria"]}:")
        print(f"talla:{dato["talla"]}:")
        print(f"Precio de producto:{dato["precio_Unitario"]}:")
        print(f"Stock de producto:{dato["stock"]}:")

codigo_solicitato= input("Ingrese codigo de producto a buscar:")
if codigo_solicitato in productos:
    product=codigo_solicitato
    print("---DETALLES DEL PRODUCTO---")
    print(f"Nombre producto:{product["nombre"]}")
    print(f"Categoria:{product["categoria"]}")
    print(f"Talla:{product["talla"]}")
    print(f"Precio:{product["precio_unitario"]}")
    print(f"stock:{product["stock"]}")
else:
    print("Producto no encontrado....")

print("---PRODUCTO POR CATEFORIA---")
print(f"Hay {mujer} productos en categoria de -Mujer-")
print(f"Hay {hombre} productos en categoria de -Hombre-")
print(f"Hay {niño} productos en categoria de -Niño-")

