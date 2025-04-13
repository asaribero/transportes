from grafo import crear_grafo
from busqueda import a_estrella
from visualizacion import mostrar_grafo
from datetime import datetime

# Diccionario de nombres opcional
nombres = {
    "A": "Portal Norte",
    "B": "Héroes",
    "C": "Calle 72",
    "D": "Calle 26",
    "E": "Calle 19",
    "F": "Universidades"
}

def mostrar_estaciones(grafo):
    print("\nEstaciones disponibles:")
    for nodo in grafo.nodes():
        print(f"- {nodo} ({nombres.get(nodo, nodo)})")

def ejecutar_pruebas(grafo):
    pruebas = [
        ("A", "F"),
        ("A", "D"),
        ("A", "E"),
        ("B", "F"),
        ("A", "Z")  # nodo no existente
    ]

    with open("pruebas.txt", "w", encoding="utf-8") as archivo:
        archivo.write("="*50 + "\n")
        archivo.write("PRUEBAS DEL SISTEMA DE BÚSQUEDA INTELIGENTE (A*)\n")
        archivo.write("Fecha de ejecución: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        archivo.write("="*50 + "\n\n")

        for i, (inicio, objetivo) in enumerate(pruebas, start=1):
            archivo.write(f"🟩 Caso {i}: Ruta desde {inicio} hasta {objetivo}\n")
            try:
                ruta, costo = a_estrella(grafo, inicio, objetivo)
                if ruta:
                    ruta_nombres = " -> ".join(nombres.get(n, n) for n in ruta)
                    archivo.write(f"Ruta óptima: {ruta_nombres}\n")
                    archivo.write(f"Costo total: {costo}\n")
                    if "C" in ruta:
                        archivo.write("Nota: Ruta pasa por estación congestionada C (+3)\n")
                else:
                    archivo.write("Resultado: No se encontró una ruta válida\n")
            except:
                archivo.write("Resultado: No se encontró una ruta válida\n")
            archivo.write("-"*50 + "\n\n")

if __name__ == "__main__":
    grafo = crear_grafo()

    while True:
        print("\n====== MENÚ DEL SISTEMA DE TRANSPORTE ======")
        print("1. Buscar una ruta")
        print("2. Mostrar mapa del grafo")
        print("3. Generar archivo de pruebas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_estaciones(grafo)
            inicio = input("Ingrese estación de origen: ").strip().upper()
            objetivo = input("Ingrese estación de destino: ").strip().upper()

            if inicio not in grafo.nodes() or objetivo not in grafo.nodes():
                print("\n❌ Estación no válida. Intente nuevamente.")
                continue

            ruta, costo_total = a_estrella(grafo, inicio, objetivo)

            if ruta:
                ruta_nombres = " -> ".join(nombres.get(n, n) for n in ruta)
                print(f"\n✅ Ruta óptima: {ruta_nombres}")
                print(f"Costo total: {costo_total}")
                if "C" in ruta:
                    print("Nota: Ruta pasa por estación congestionada C (+3)")
            else:
                print("\n❌ No se encontró una ruta válida.")

        elif opcion == "2":
            mostrar_grafo(grafo)

        elif opcion == "3":
            ejecutar_pruebas(grafo)
            print("\n✅ Archivo pruebas.txt generado correctamente.")

        elif opcion == "4":
            print("Saliendo del sistema. ¡Gracias!")
            break

        else:
            print("Opcion no válida. Intente de nuevo.")
