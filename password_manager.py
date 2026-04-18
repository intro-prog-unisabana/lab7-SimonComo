import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    pass


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    pass


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass

import csv
from caesar import caesar_encrypt


# Parte 1
def encrypt_single_pass(filename):
    # leer contraseña
    with open(filename, "r") as file:
        password = file.read().strip()

    # encriptar
    encrypted = caesar_encrypt(password)

    # sobrescribir archivo
    with open(filename, "w") as file:
        file.write(encrypted)


# Parte 2A y 2B
def encrypt_passwords_in_file(filename):
    rows = []

    # leer archivo
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # evitar líneas vacías
                rows.append(row)

    # encriptar solo contraseñas (columna 2)
    for i in range(1, len(rows)):  # saltar encabezado
        password = rows[i][2]
        rows[i][2] = caesar_encrypt(password)

    # escribir de nuevo
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


# Parte 3
def change_password(filename, website, password):
    rows = []
    found = False

    # leer
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                rows.append(row)

    # buscar y cambiar
    for i in range(1, len(rows)):
        if rows[i][0] == website:
            rows[i][2] = caesar_encrypt(password)
            found = True
            break

    if not found:
        return False

    # escribir cambios
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return True


# Parte 4
def add_login(filename, website_name, username, password):
    encrypted = caesar_encrypt(password)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted])