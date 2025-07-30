productos= {}

numeros_productos= int(input("Ingrese cantidad de productos a ingresar:"))

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
        print(f"Nombre de producto:{dato["categoria"]}:")
        print(f"Nombre de producto:{dato["talla"]}:")
        print(f"Nombre de producto:{dato["precio_Unitario"]}:")
        print(f"Nombre de producto:{dato["stock"]}:")


