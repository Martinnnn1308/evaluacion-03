import os

Especies = ["Perros", "Gatos", "Aves"]

Registros = []

def Registrar():
    while True:
        try:
            os.system("cls")
            nom = input("Ingrese el nombre de la mascota\n> ")

            if len(nom) < 2:
                input("El nombre no puede estar vacio o es muy corto")
                continue

            nom = nom.lower()

            aux = 1
            os.system("cls")
            print("--- Categorias ---")
            for nombre in Especies:
                print(f"{aux}) {nombre}")
                aux += 1
            
            especie = int(input("\n> "))

            especie = Especies[especie - 1]

            os.system("cls")
            
            peso = float(input("Ingrese el peso de la mascota (KG)\n> "))

            if peso < 0.4 or peso > 100:
                input("El peso no puede ser negativo o menor a 0.4 o mayor a 20")
                continue

            peso = f"{peso:.2f}"

            costo = 10000

            impuesto_salud = costo * 0.05

            impuesto_salud = int(impuesto_salud)

            costo_total = costo + impuesto_salud

            costo_total = int(costo_total)

            lista_aux = [nom, especie, peso, costo, impuesto_salud, round(costo_total)]

            Registros.append(lista_aux)

            break

        except:
            input("Error en el ingreso de datos, vuelva a intentarlo")
            continue

def ListarMascotasRegistradas():
    while True:
        try:
            os.system("cls")
            print("-------------------------------------------------------------------------------------")
            print("| Nombre    |   Especie    |   Peso(KG)  |   Costo    |   Salud    |   Costo Total  |")
            print("-------------------------------------------------------------------------------------")
            for animal in Registros:
                
                print(f"| {animal[0]:^7s}   |   {animal[1]:^8s}   |   {animal[2]:^7s}   |   {animal[3]:^6d}   |   {animal[4]:^5d}   |   {animal[5]:^5d}         |")

            salir = input("\n\nVolver Al Menu\n> [ENTER] ")
            break
            
        except:
            input("Error en el ingreso de datos, vuelva a intentarlo")

def Imprimir():
    while True:
        try:
            os.system("cls")
            with open("impresion.txt", "w") as archivo:
                archivo.write("----------------------------------------------------------------------------------\n")
                archivo.write("| Nombre    |   Especie    |   Peso    |   Costo    |   Salud    |   Costo Total |\n")
                archivo.write("----------------------------------------------------------------------------------\n")
                for animal in Registros:
                    archivo.write(f"| {animal[0]:^7s}   |   {animal[1]:^8s}   |   {animal[2]:^7s}   |   {animal[3]:^6d}   |   {animal[4]:^5d}   |   {animal[5]:^5d}      |\n")
                
                print("¡Archivo Creado Correctamente!")

                salir = input("\n\nVolver Al Menu\n> [ENTER] ")
                break
        except:
            input("Error en el ingreso de datos, vuelva a intentarlo")

    

def ImprimirXEspecie():
    while True:
        try:
            aux = 1
            os.system("cls")
            print("--- Categorias ---")
            for nombre in Especies:
                print(f"{aux}) {nombre}")
                aux += 1

            especie = int(input("> "))

            especie = Especies[especie - 1]

            with open("Impresion.txt", "w") as archivo:
                archivo.write("----------------------------------------------------------------------------------\n")
                archivo.write("| Nombre    |   Especie    |   Peso    |   Costo    |   Salud    |   Costo Total |\n")
                archivo.write("----------------------------------------------------------------------------------\n")
                for animal in Registros:
                    if especie == animal[1]:
                        archivo.write(f"| {animal[0]:^7s}   |   {animal[1]:^8s}   |   {animal[2]:^7s}   |   {animal[3]:^6d}   |   {animal[4]:^5d}   |   {animal[5]:^5d}      |\n")
                
            print("¡Archivo Creado Correctamente!")

            salir = input("\n\nVolver Al Menu\n> [ENTER] ")
            break

        except:
            input("Error en el ingreso de datos, vuelva a intentarlo")



def main():
    while True:
        try:
            os.system("cls")
            print("------- MENU ----------")
            print("1) Registrar Mascota")
            print("2) Enlistar Mascotas Registradas")
            print("3) Imprimir Mascotas Registradas")
            print("4) Imprimir Mascotas Registradas Por Especie")
            print("5) Salir")
            opcion = int(input("> "))
            
            if opcion == 1:
                Registrar()
            elif opcion == 2:
                ListarMascotasRegistradas()
            elif opcion == 3:
                Imprimir()
            elif opcion == 4:
                ImprimirXEspecie()
            elif opcion == 5:
                print("¡Adios!")
                break
            else:
                input("¡Opcion Invalida!")

        except:
            input("Error en el ingreso de datos, vuelva a intentarlo")

if __name__ == "__main__":
    main()