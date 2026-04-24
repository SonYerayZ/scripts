#!/usr/bin/env python3
import subprocess
import sys
import re


def run_nmap(ip: str) -> None:
    print(f"[*] Escaneando {ip} con nmap -sV -sC ...")

    try:
        resultado = subprocess.run(
            ["nmap", "-sV", "-sC", ip],
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        print("[!] Error: nmap no está instalado o no se encuentra en el PATH.")
        sys.exit(1)

    output = resultado.stdout

    # Buscar si hay puertos abiertos en el output
    puertos_abiertos = re.search(r"(\d+)/\w+\s+open", output)

    if not puertos_abiertos:
        print("[!] NO HAY NINGUN PUERTO ABIERTO")
        return

    # Guardar (sobreescribir) el resultado en el archivo
    nombre_archivo = "nmap_escaneo.txt"
    with open(nombre_archivo, "w") as f:
        f.write(output)

    print(f"[+] Escaneo completado. Resultados guardados en '{nombre_archivo}'.")
    print(output)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ip = sys.argv[1]
    else:
        ip = input("Introduce la IP o hostname a escanear: ").strip()

    if not ip:
        print("[!] Error: debes introducir una IP o hostname.")
        sys.exit(1)

    run_nmap(ip)
