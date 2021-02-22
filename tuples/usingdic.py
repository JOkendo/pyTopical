contacts = {}
done = True
while done:
    choice = input("A)dd, D)elete, L)ook up, I)nfo, Q)uit: ")
    if choice == 'A' or choice == 'a':
        name = input("Name: ")
        phone = input("Number for "+ name + " : ")
        contacts[name] = phone
    elif choice == 'D' or choice == 'd':
        name = input("Enter name:")
        del contacts[name]
    elif choice == 'L' or choice == 'l':
        name = input("Name to search : ")
        print(name,contacts[name])
    elif choice == 'I' or choice == 'i':
        print(contacts)
    elif choice == 'Q' or choice == 'q':
        done = False
    else:
        print(choice, ' is invalid')