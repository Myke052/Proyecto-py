#Funciones definidas
def showListEmp(a,b):
    print("\nLista de empleados\nItem Nombre                                  Cargo")
    for x in range(0,len(a)): #Con este ciclo se organizan los datos de las listas para visaulizarlos de forma vertical.
        print("{:5}{:40}{:2}".format(str(x+1),a[x],b[x])) #El iterador del ciclo recorre cada posición de las listas y muestra en pantalla el contenido por filas y cada lista es una columna.

def showListProd(a,b,c):
    print("\nLista de productos\nItem Descripción                           Cant      Precio")
    for x in range(0,len(a)):
        print("{:5}{:30}{:12}{:12}".format(str(x+1),a[x],b[x],c[x]))

def showListTabl(a):
    print("\nListado de mesas\nItem Descripción Estado")
    for x in range (0,len(a)):
        print("{:5}{:30}".format(str(x+1),a[x]))

from os import system #Libreria que permite usar la funcion Limpiar consola

#Listas donde se almacena la infomación mientras el programa esta en ejecución
empleados = [] #Corresponde a la lista donde se guardarán los empleados creados por el administrador
cargos = [] #Corresponde a la lista donde se guardarán los cargos de los empleados creadas por el administrador
productos = [] #Inventario
cantidades = [] #Cantidades de los productos en inventario
cantVentas = [] #lista de las cantidades vendidas de cada producto del inventario
'''¡¡¡IMPORTANTE!!! con respecto a la lista cantVentas
Esta lista se debe llenar con ceros por debajo (a través de código) cuando se esten creando los productos 
debido a que no es posible alimentarla usando indices "posiciones" que no existen dentro de la lista vacia (si se deja vacia), 
si se usa la funcion ".insert" con un indice mayor a cero guarda el dato en la primera posición vacia; Llenando 
las posiciones con ceros se garantiza una posición de cantidades vendidas para cada producto de la lista 
cuya posición corresponde a la posición del producto y así se puede restar con seguridad la cantidad vendida 
que corresponde a cada producto de las listas productos y cantidades'''
precios = [] #Precios de los producto
mesas=["Mesa #1     Disponible","Mesa #2     Disponible","Mesa #3     Disponible","Mesa #4     Disponible",
        "Mesa #5     Disponible","Mesa #6     Disponible","Mesa #7     Disponible","Mesa #8     Disponible",
        "Mesa #9     Disponible","Mesa #10     Disponible","Mesa #11     Disponible","Mesa #12     Disponible",
        "Mesa #13     Disponible","Mesa #14     Disponible","Mesa #15     Disponible","Mesa #16     Disponible"] #Lista de meses predeterminada

system ("cls") #Se limpia consola para inciciar con el promer menu

print("-------------------------------------------------------------------------------------------------------\n")
print("Bienvenido al sistema de información de Enjoys DSC")
repetir=1
while repetir==1:
    while True:
        try:
            tUser = int(input("\nPor favor seleccione su rol para iniciar:\n1-Si es usuario ADMINISTRADOR\n2-Si es usuario estándar\n-Cualquier otro número para salir\n")) #lee la entrada del usuario con respecto al tipo de usuario que desea acceder al programa
            break
        except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
    if tUser==1: #Inicio de sesión como ADMIN
        intentos=3
        while intentos>0 and intentos<=3:
            ingUs=input("\n-------------------------------------------------------------------------------------------------------\n\nHa seleccionado ingresar como ADMINISTRADOR por favor ingrese las credenciales correspondientes.\nUser: ") #User administrador ingresado por el usuario
            ingPas=input("Pass: ") #Password del user del administrador ingresado por el usuario
            intentos-= 1
            if ingUs=="gef" and ingPas=="123": intentos=0 #User y Password del administrador
            else: print("Las credenciales ingresadas son incorrectas, por favor intente de nuevo.")

        repetir=1
        while repetir==1:
            if ingUs=="gef" and ingPas=="123":
                while True:
                    try:
                        opcOper=int(input("\nMenú de usuario ADMIN\n1-Crear empleado\n2-Modificar/Eliminar empleado\n3-Consultar lista de empleados\n4-Crear producto\n5-Modificar/Eliminar producto\n6-Consultar lista de productos\n7-Asignar mesas en mantenimiento\n-Cualquier otro número para salir\n"))
                        break
                    except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                if opcOper==1: #Opción para crear empleado
                    event = 1 #La variable event significa "evento" y hace referencia a una accion como crear, modificar o eliminar.
                    while event==1:
                        while True:
                            try:
                                event=int(input("\n¿Requiere crear un nuevo empleado?\n1-SI\n-Cualquier otro número para salir\n"))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        if event==1:
                            empleados.append(input("\nIngrese el nombre del empleado a crear: "))
                            cargos.append(input("Ingrese el cargo del empleado creado: "))
                elif opcOper==2 and len(empleados)>0: #Opción para modificar/eliminar empleado
                    event=1
                    while event==1 or event==2:
                        while True:
                            try:
                                event=int(input("\n¿Requiere modificar o eliminar un empleado?\n1-Para modificar empleado\n2-Para eliminar empleado\n-Cualquier otro número para salir\n"))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        if event==1: #Opción para modificar empleado
                            showListEmp(empleados,cargos)
                            while True:
                                try:                                    
                                    elecc=int(input("\nSegún la lista anterior, ¿cual empleado requiere modificar?\nPor favor ingrese el número del ítem del empleado que requiere modificar: "))
                                    if elecc>0 and elecc<=len(empleados): break
                                    print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                                except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                            print("El empleado seleccionado es",empleados[elecc-1])
                            while True:
                                try:
                                    confirmacion=int(input("\n¿Esta seguro de modificar el empleado?\n1-SI\n-Cualquier otro número para NO\n"))
                                    break
                                except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                            if confirmacion==1:
                                empleados[elecc-1]=input("\nIngrese el nuevo nombre del empleado: ")
                                cargos[elecc-1]=input("Ingrese el nuevo cargo del empleado: ")
                            else: event==1
                        elif event==2: #Opción para eliminar empleado
                            showListEmp(empleados,cargos)
                            while True:
                                try:
                                    elecc=int(input("\nSegún la lista anterior, ¿cual empleado requiere eliminar?\nPor favor ingrese el ítem del empleado que requiere eliminar: "))
                                    if elecc>0 and elecc<=len(empleados): break
                                    print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                                except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                            print("El empleado seleccionado es",empleados[elecc-1])
                            while True:
                                try:
                                    confirmacion=int(input("\n¿Esta seguro de eliminar el empleado?\n1-SI\n-Cualquier otro número para NO\n"))
                                    break
                                except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                            if confirmacion==1:
                                empleados.remove(empleados[elecc-1])
                                cargos.remove(cargos[elecc-1])
                            else: event==2
                elif opcOper==3: #Opción para consultar lista de empleados
                    showListEmp(empleados,cargos)
                elif opcOper==4: #Opción para crear producto
                    event = 1
                    while event == 1:
                        while True:
                            try:
                                event=int(input("\n¿Requiere crear un nuevo producto?\n1-SI\n-Cualquier otro número para salir\n"))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        if event == 1: #Crear Producto
                            productos.append(input("\nIngrese el nombre del producto a crear: "))
                            cantidades.append(int(input("Ingrese la cantidad de unidades existentes del producto creado: ")))
                            while True:
                                try:
                                    precios.append(int(input("Ingrese el precio unitario del producto creado: ")))
                                    break
                                except:print("El tipo de dato ingresado es incorrecto, ingrese números enteros")
                            cantVentas.append(0)
                elif opcOper==5 and len(productos)>0: #Opción para modifcar/eliminar producto
                    event = 1 
                    while event==1 or event==2:
                        while True:
                            try:
                                event=int(input("\n¿Requiere modificar o eliminar un producto?\n1-Para modificar producto\n2-Para eliminar producto\n-Cualquier otro número para salir.\n"))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        if event==1: #Opcion para moficar producto
                            showListProd(productos,cantidades,precios)
                            while True:
                                try:
                                    elecc=int(input("\nSegún la lista anterior, ¿cual producto desea modificar?\nPor favor ingrese el número del ítem del producto que requiere modificar: "))
                                    if elecc>0 and elecc<=len(productos): break
                                    print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                                except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                            print("El producto seleccionado es",productos[elecc-1])
                            while True:
                                try:
                                    confirmacion=int(input("\n¿Esta seguro de modificar el producto seleccionado?\n1-SI\n-Cualquier otro número para NO\n"))
                                    break
                                except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                            if confirmacion==1:
                                while True:
                                    try:
                                        opcOper = int(input ("\nIngrese una opción:\n1-Para editar la descripción del producto\n2-Para editar la cantidad del producto\n3-Para editar el precio del producto\n-Cualquier otro número para regresar al menú anterior\n"))
                                        break
                                    except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                                if (opcOper == 1): #opción para modificar descripción
                                    while True:
                                        productos[elecc-1]=input("\nIngrese el nuevo nombre del producto: ")
                                        if len(productos[elecc-1])==0: print("\nNo se ingreso dato alguno, por favor intentelo otra vez")
                                        else: break
                                    print("\nLA EDICIÓN FUE EXITOSA!!!\n") 
                                elif(opcOper == 2):
                                    while True:
                                        try:
                                            cantidades[elecc-1]=int(input("\nIngrese la nueva cantidad del producto: "))
                                            if cantidades[elecc-1]>=0:break                                      
                                        except: print("\nNo se ingreso dato correcto, por favor intentelo otra vez")
                                    print("\nLA EDICIÓN FUE EXITOSA!!!\n")  
                                elif(opcOper==3):
                                    while True:
                                        try:
                                            precios[elecc-1]=int(input("\nIngrese el nuevo precio del producto: "))
                                            if precios[elecc-1]>=0:break                                    
                                        except: print("\nNo se ingreso dato correcto, por favor intentelo otra vez")
                                    print("\nLA EDICIÓN FUE EXITOSA!!!\n")                                                                            
                       
                        elif event==2: #Opción para eliminar producto
                            showListProd(productos,cantidades,precios)
                            while True:
                                try:
                                    elecc=int(input("\nSegún la lista anterior, ¿cual producto desea eliminar?\nPor favor ingrese el número del ítem del producto: "))
                                    if elecc>0 and elecc<=len(productos): break
                                    print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                                except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                            print("El producto seleccionado es",productos[elecc-1])
                            while True:
                                try:
                                    confirmacion=int(input("\n¿Esta seguro de eliminar el producto seleccionado?\n1-SI\n-Cualquier otro número para NO\n"))
                                    break
                                except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                            if confirmacion==1:
                                productos.remove(productos[elecc-1])
                                cantidades.remove(cantidades[elecc-1])
                                precios.remove(precios[elecc-1])
                                cantVentas.remove(cantVentas[elecc-1])                               
                            print("\nLA ELIMINACIÓN DE PRODUCTO FUE EXITOSA!!!\n")                         

                elif opcOper==6: #Opción para consultar lista de productos
                    showListProd(productos,cantidades,precios)
                elif opcOper==7: #Opcion para inhabilitar mesas en mantenimiento
                    repetir=1
                    while repetir==1:
                        while True:
                            try:
                                opcOper=int(input("\nMenú de asignación de mesas en mantenimiento\n1-Inhabilitar mesa\n2-Habilitar mesa\n3-Consultar estado de las mesas\n-Cualquier otro número para salir\n"))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        if opcOper==1: #Opción para ihabilitar mesas
                            showListTabl(mesas)
                            while True:
                                try:
                                    elecc=int(input("\nSegún la lista anterior ingrese el número del ítem de la mesa que requiere inhabilitar: ")) #Para leer eleccion de mesa
                                    if elecc>0 and elecc<=len(mesas): break                                    
                                except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                            if mesas[elecc-1]=="Mesa #"+str(elecc)+"     Disponible":
                                mesas[elecc-1]="Mesa #"+str(elecc)+"     En mantenimiento"
                                print("\nHa inhabilitado por mantenimiento la Mesa #"+str(elecc))                                
                            else: print("\nLa mesa seleccionada esta reservada o en mantenimiento, debe seleccionar una mesa disponible")
                        elif opcOper==2: #Opción para que cambie el estado de las mesas de la lista a Disponible
                            showListTabl(mesas)
                            while True:
                                try:
                                    elecc=int(input("\nSegún la lista anterior ingrese el número del ítem de la mesa que requiere liberar: ")) #Para leer eleccion de mesa
                                    if elecc>0 and elecc<=len(mesas) and mesas[elecc-1]=="Mesa #"+str(elecc)+"     En mantenimiento":
                                        mesas[elecc-1]="Mesa #"+str(elecc)+"     Disponible"
                                        print("\nLa Mesa #"+str(elecc)+" ha cambiado su estado a Disponible")
                                        break
                                    else:
                                        print("\nLa mesa seleccionada no esta en mantenimiento")
                                        break                                  
                                except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido ")
                        elif opcOper==3: #Opción para consultar las mesas y su estado
                            showListTabl(mesas) 
                        while True:
                            try:
                                repetir=int((input("\n¿Desea volver al menú anterior?\n1-Para si\n-Cualquier otro número para salir\n")))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")                                            
                else:
                    if opcOper==2: print("No hay empleados creados")
                    if opcOper==5: print("No hay productos creados")
                while True:
                    try:
                        repetir=int(input("\n¿Desea regresar al menú de usuario ADMIN?\n1-SI\n-Cualquier otro número para salir\n"))
                        break
                    except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
            else:
                print("\nDemasiados intentos fallidos, para volver a intentar regrese al menú anterior")
                break
    elif tUser==2 and len(empleados)>0: #Inicio de sesión como usuario estándar
        intentos=3 
        while intentos>0 and intentos<=3: 
            ingUs=input("\n-------------------------------------------------------------------------------------------------------\n\nHa seleccionado ingresar como usuario estándar por favor ingrese las credenciales correspondientes.\nNombre del empleado: ") #Usuario del empleado ingresado por el usuario
            ingPas=input("Cargo: ") #Cargo del empleado ingresado por el usuario
            intentos-=1
            if ingUs in empleados and ingPas in cargos: intentos=0 #User y Cargo del empleado
            else: print("Las credenciales ingresadas son incorrectas, por favor intente de nuevo.")

        repetir=1
        while repetir==1:
            if ingUs in empleados and ingPas in cargos:
                while True:
                    try:
                        opcOper=int(input("\nMenú de usuario estándar\n1-Vender productos\n2-Reservar o liberar mesas\n-Cualquier otro número para salir\n"))
                        break
                    except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                if opcOper==1: #Opción para vender productos
                    repetir=1
                    while repetir==1:
                        while True:
                            try:
                                opcOper=int(input("\nMenú para venta de productos\n1-Vender producto\n2-Consultar productos, cantidades disponibles y precios\n-Cualquier otro número para salir\n"))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        if opcOper==1 and len(productos)>0: #Opción para vender producto
                            repetir=1
                            while repetir==1:
                                showListProd(productos,cantidades,precios)
                                while True:
                                    try:
                                        elecc=int(input("\nSegún la lista anterior, por favor ingrese el número del ítem del producto que requiere vender: ")) #Para leer eleccion de producto
                                        if elecc>0 and elecc<=len(productos): break
                                        print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")
                                    except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido") 
                                print("El producto seleccionado es",productos[elecc-1],"el cual cuenta con",cantidades[elecc-1],"unidades disponibles")
                                if cantidades[elecc-1]>0:
                                    while True:
                                        try:
                                            unidven=int(input("Ingrese la cantidad vendida: "))
                                            if unidven>=0 and unidven<=cantidades[elecc-1]: break
                                            print("La cantidad ingresada supera las unidades disponibles.\nPor favor ingrese una cantidad válida")
                                        except:print("El tipo de dato ingresado es incorrecto, ingrese números enteros")
                                    cantVentas[elecc-1]=unidven
                                    cantidades[elecc-1]-=cantVentas[elecc-1]
                                    print("La venta del producto seleccionado fue registrada con éxito")
                                else: print("El producto no tiene unidades disponibles para la venta")
                                while True:
                                    try:
                                        repetir=int(input("\n¿Requiere vender otro producto?\n1-SI\n-Cualquier otro número para salir\n"))
                                        break
                                    except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        elif opcOper==2: #Opción para consultar los productos, cantidades disponibles y precios
                            showListProd(productos,cantidades,precios)
                        else: 
                            if opcOper==1:print("No hay productos creados")
                        while True:
                            try:
                                repetir=int((input("\n¿Desea volver al menú anterior?\n1-Para si\n-Cualquier otro número para salir\n")))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                elif opcOper==2: #Opción para reservar o liberar mesas
                    repetir=1
                    while repetir==1:
                        while True:
                            try:
                                opcOper=int(input("\nMenú para reservación y liberación de mesas\n1-Reservar mesa\n2-Liberar mesa\n3-Consultar estado de las mesas\n-Cualquier otro número para salir\n"))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                        if opcOper==1: #Opción para que cambie el estado de las mesas de la lista a Reservada
                            showListTabl(mesas)
                            while True:
                                try:
                                    elecc=int(input("\nSegún la lista anterior ingrese el número del ítem de la mesa que requiere reservar: ")) #Para leer eleccion de mesa
                                    if elecc>0 and elecc<=len(mesas) and mesas[elecc-1]=="Mesa #"+str(elecc)+"     Disponible":
                                        mesas[elecc-1]=="Mesa #"+str(elecc)+"     Disponible"
                                        mesas[elecc-1]="Mesa #"+str(elecc)+"     Reservada"
                                        print("\nLa mesa seleccionada ha sido reservada con éxito")
                                        break
                                    else:
                                        print("\nLa mesa seleccionada no esta disponible!!!")
                                        break
                                except: print("El ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")                                                       
                        elif opcOper==2: #Opción para que cambie el estado de las mesas de la lista a Disponible
                            showListTabl(mesas)
                            while True:
                                try:
                                    elecc=int(input("\nSegún la lista anterior ingrese el número del ítem de la mesa que requiere liberar: ")) #Para leer eleccion de mesa
                                    if elecc>0 and elecc<=len(mesas) and mesas[elecc-1]=="Mesa #"+str(elecc)+"     Reservada":
                                        mesas[elecc-1]="Mesa #"+str(elecc)+"     Disponible"
                                        print("La Mesa #"+str(elecc)+" ha cambiado su estado a Disponible")
                                        break
                                    else:
                                        print("\nEl ítem ingresado no esta reservado!!! ")
                                        break
                                except: print("\nEl ítem ingresado no esta dentro de la lista, por favor ingrese un ítem válido")                            
                        elif opcOper==3: #Opción para consultar las mesas y su estado
                            showListTabl(mesas)
                        while True:
                            try:
                                repetir=int((input("\n¿Desea volver al menú anterior?\n1-Para si\n-Cualquier otro número para salir\n")))
                                break
                            except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
                while True:
                    try:
                        repetir=int(input("\n¿Desea regresar al menú de usuario estándar?\n1-SI\n-Cualquier otro número para salir\n"))
                        break
                    except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")
            else:
                print("\nDemasiados intentos fallidos, para volver a intentar regrese al menú anterior.")
                break
    else:
        if tUser==2: 
            print("No hay empleados creados")
    while True:
        try:
            repetir=int(input("\n¿Desea regresar al menú de selección de usuario?\n1-SI\n-Cualquier otro número para salir del sistema\n"))
            break
        except: print("La opción ingresada es incorrecta, por favor ingrese una opción válida")

print("\nEsperamos que regrese pronto....")