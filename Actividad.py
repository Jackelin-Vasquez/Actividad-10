productos= {}

numeros_productos= int(input("Ingrese cantidad de productos a ingresar:"))

for  producto in range(numeros_productos):
    print(f"---Producto no.{producto +1}")
    codigo= input("Ingrese codigo de producto:")
    nombre= input("Ingrese nombre de producto:").lower()
    categoria= input("Ingrese categoria (Hombre, Mujer, Niño):").lower()
    talla= input("Ingrese talla (S,M,L,XL) :").lower()
    Precio_unitario= float(input("Ingrese precio:"))
    stock= int(input("Ingrese cantidad de stock de producto:"))

    productos[codigo]= {
        "Nombre":nombre,
        "Categoria": categoria,
        "talla":talla,
        "Precio_Unitario": Precio_unitario,
        "Stock":stock

    }