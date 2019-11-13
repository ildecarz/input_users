print('Welcome to my new program!!!\n')
print('Select one option:\n')
print('1) Insert new user')
print('2) Show all database')
print('3) Delete user')

choice = input('Select an option: ')


with open('userdb.csv', 'r') as db: #crea un archivo vacio
    db_list = db.readlines()



def add_new_user():
    with open('userdb.csv', 'w') as db:
        for user in db_list:
            db.writelines(user) #edita el archivo creado
        print('Complete this information')
        name = input('Name: ')
        last_name = input('Last name: ')
        phone = input('Phone: ')
        address = input('Address: ')
        db.write(f'{name},{last_name},{phone},{address}\n')
        print('A new user has been created!!!')

def show_database():
    for l in db_list:
        l_split = l.split(',')
        print(f'Name: {l_split[0]}, Last Name: {l_split[1]}, Phone: {l_split[2]}, Address: {l_split[3]}')
        print('......................................................................')

def deleted_user():
    with open('userdb.csv', 'w') as db:
        print('Complete this information')
        name = input('Name: ')
        last_name = input('Last name: ')
        for d in db_list:
            d_split = d.split(',')
            if name == d_split[0] and last_name == d_split[1]:
                print(f'User {d_split[0]} {d_split[1]} has been removed!!! ')
            else:
                db.writelines(d)
        show_database()

if choice == '1':
    add_new_user()
elif choice == '2':
    show_database()
elif choice == '3':
    deleted_user()
else:
    print('Not implemented option')




