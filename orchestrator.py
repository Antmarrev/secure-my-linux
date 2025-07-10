#!/usr/bin/env python3

import subprocess

def menu():
    print("+----------------------------------------------------+")
    print("| 🛡️ Secure My Linux - Instalador Seguro              |")
    print("+----------------------------------------------------+")
    print("| Bienvenido, selecciona la opción que deseas:      |")
    print("| 1) Actualizar sistema y paquetes                  |")
    print("| 2) Configurar firewall (UFW)                      |")
    print("| 3) Configurar SSH seguro                          |")
    print("| 4) Crear usuario no-root con permisos sudo        |")
    print("| 5) Instalar herramientas de seguridad             |")
    print("| 6) Aplicar todas las configuraciones automáticamente |")
    print("| 0) Salir                                          |")
    print("+----------------------------------------------------+")

def main():
    while True:
        menu()
        choice = input("Selecciona una opción: ")
        if choice == "1":
            print("[INFO] Ejecutando actualización del sistema...")
            # subprocess.call(["bash", "scripts/update_system.sh"])
            print("[DEV] Funcionalidad en desarrollo.")
        elif choice == "2":
            print("[INFO] Configurando firewall (UFW)...")
            print("[DEV] Funcionalidad en desarrollo.")
        elif choice == "3":
            print("[INFO] Configurando SSH seguro...")
            print("[DEV] Funcionalidad en desarrollo.")
        elif choice == "4":
            print("[INFO] Creando usuario no-root con sudo...")
            print("[DEV] Funcionalidad en desarrollo.")
        elif choice == "5":
            print("[INFO] Instalando herramientas de seguridad...")
            print("[DEV] Funcionalidad en desarrollo.")
        elif choice == "6":
            print("[INFO] Aplicando todas las configuraciones automáticamente...")
            print("[DEV] Funcionalidad en desarrollo.")
        elif choice == "0":
            print("[INFO] Saliendo...")
            break
        else:
            print("[ERROR] Opción no válida, inténtalo de nuevo.")

if __name__ == "__main__":
    main()