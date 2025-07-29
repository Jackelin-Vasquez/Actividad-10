productos= {}

numeros_productos= int(Input("Ingrese cantidad de productos a ingresar:"))

for  producto in range(numeros_productos):
    print(f"---Producto no.{producto +1}")
    codigo= input("Ingrese codigo de producto:")
    nombre= input("Ingrese nombre de producto:")
    categoria= input("Ingrese categoria:")
    talla= input("Ingrese talla:")
    Precio_unitario= float(input("Ingrese precio:"))
