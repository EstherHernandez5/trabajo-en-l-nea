productos = []

def mostrar_menu():
    print("\nMenú:")
    print("[1] Registrar Producto")
    print("[2] Modificar Producto")
    print("[3] Eliminar Producto")
    print("[4] Consultar Producto")
    print("[5] Salir del programa")

def registrar_producto():
    producto = input("Nombre del producto a registrar: ")
    productos.append(producto)
    print(f"Producto '{producto}' registrado.")

def modificar_producto():
    producto_a_modificar = input("Nombre del producto a modificar: ")
    if producto_a_modificar in productos:
        nuevo_producto = input("Introduce el nuevo nombre del producto: ")
        indice = productos.index(producto_a_modificar)
        productos[indice] = nuevo_producto
        print(f"Producto '{producto_a_modificar}' modificado a '{nuevo_producto}'.")
    else:
        print("El producto no se encuentra en la lista.")

def eliminar_producto():
    producto_a_eliminar = input("Nombre del producto a eliminar: ")
    if producto_a_eliminar in productos:
        productos.remove(producto_a_eliminar)
        print(f"Producto '{producto_a_eliminar}' eliminado.")
    else:
        print("El producto no se encuentra en la lista.")

def consultar_productos():
    if productos:
        print("Lista de productos registrados:")
        for producto in productos:
            print(f"- {producto}")
    else:
        print("No hay productos registrados.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            modificar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            consultar_productos()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()