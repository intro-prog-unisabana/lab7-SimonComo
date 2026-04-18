from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    pass


if __name__ == "__main__":
    main()

from password_manager import (
    encrypt_passwords_in_file,
    change_password,
    add_login
)

# 1. pedir archivo
filename = input("Enter the CSV file name:\n")

# 2. encriptar todo al inicio
encrypt_passwords_in_file(filename)

# 3. menú
while True:
    option = input("Options: (1) Change Password, (2) Add Password, (3) Quit:\n")

    # OPCIÓN 1
    if option == "1":
        data = input("Enter the website and the new password:\n").split()

        if len(data) < 2:
            print("Input is in the wrong format!")
            continue

        website, password = data[0], data[1]

        if len(password) < 12:
            print("Password is too short!")
            continue

        result = change_password(filename, website, password)

        if not result:
            print("Website not found! Operation failed.")
        else:
            print("Password changed.")

    # OPCIÓN 2
    elif option == "2":
        data = input("Enter the website, username, and password:\n").split()

        if len(data) < 3:
            print("Input is in the wrong format!")
            continue

        website, username, password = data[0], data[1], data[2]

        if len(password) < 12:
            print("Password is too short!")
            continue

        add_login(filename, website, username, password)
        print("Login added.")

    # OPCIÓN 3
    elif option == "3":
        break

    # OPCIÓN INVÁLIDA
    else:
        print("Invalid option selected!")