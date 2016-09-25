# ==================================================================
# Proponuję zrobie klasy  reprezentującą pojedynczy wpis do tej książki, oraz klasę do reprezentowania całej książki (wykorzystywany będzie tylko jej jeden obiekt).
# ==================================================================
#nawigacja ma byc przez podawanie numeru akcji
# np. jak uzytkownik wpisze 1, to bedziemy przegladac wpisy
# a jak EDYTUJ 1, to przejdziemy do edycji pierwszego wpisu


class Entry:

    def __init__(self, name, last_name, phone_nr):
        self.name = name
        self.last_name = last_name
        self.phone_nr = phone_nr

                        # ****************** NEW ENTRY FUNCTION *******************
    @staticmethod
    def new():
        while True:
            entries_counter = 0
            print('In order to create new Phone Book record, please enter some data.')
            name = input('Name: ')
            last_name = input('Last Name: ')
            phone_number = input('Phone Number: ')
            print('New entry has been successfully added!')
            return Entry(name, last_name, phone_number)



                                        #************ EDIT LOOP **********
    # def edit(self):
        #petla do edytowania wpisu



    # do tworzenia nowego obiektu Entry
    # return Entry(tutaj dane)


class Phonebook:
    def __init__(self, vol):
        self.vol_number = vol

    @staticmethod
    def browse(self):
        pass
        #petla do przegladaia wpisów

        #edycji istiejacych
        #i dodawnia nowych


def show_menu():
    print('\nWhat do you want to do? \n\nEnter 1 to CREATE new Entries \nEnter 2 to EDIT existing Entries')
    print('Enter 3 to BROWSE Entries \nEnter 4 to exit PhoneBook ')

# ***************** MAIN LOOP *****************
while True:
    show_menu()
    chosen_menu_option = int(input())
    # =============================================
    if chosen_menu_option == 1:
        Entry.new()
    elif chosen_menu_option == 2:
        # edit_entry()
        break
    elif chosen_menu_option == 3:
        print('\nHere you\'ll see "browse()" function')
        # browse()
        break

    elif chosen_menu_option == 4:
        print('\nThe PhoneBook has ended. Thanks and see you next time!')
        break



#
# Phonebook_1 = Phonebook(1)
# record1 = Entry('Zosia', 'Kornafel', 789789798)
#
# print('Volume number: ', Phonebook_1.vol_number)
# print(record1.name, record1.last_name, record1.phone_nr)