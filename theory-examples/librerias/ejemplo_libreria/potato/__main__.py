import csv
import argparse

def main():
    parser = argparse.ArgumentParser(description="Leer un archivo CSV de canciones")
    parser.add_argument("-f", "--file", required=True, help="Nombre del archivo CSV")
    parser.add_argument("-o", "--output", required=True, help="Nombre del archivo CSV")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for cancion in lector:
            print(f"Título: {cancion['titulo']}")
            print(f"Artista: {cancion['artista']}")
            print(f"Álbum: {cancion['album']}")
            print("-" * 20)

if __name__ == "__main__":
    main()