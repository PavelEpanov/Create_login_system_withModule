import login

def main():

    firstName = input("Введите ваше имя: ")
    lastName = input("Введите вашу фамилию: ")
    number = input("Введите ваш номер: ")

    set_login = login.get_data(firstName=firstName, lastName=lastName, Number=number)

    print(set_login)

main()