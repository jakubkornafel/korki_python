# ==================================================================
# Proponuję zrobić klasę reprezentującą pojedynczy wpis do tej książki, oraz klasę do reprezentowania całej książki (wykorzystywany będzie tylko jej jeden obiekt).
# ==================================================================
#nawigacja ma byc przez podawanie numeru akcji
# np. jak uzytkownik wpisze 1, to bedziemy przegladac wpisy
# a jak EDYTUJ 1, to przejdziemy do edycji pierwszego wpisu


class Entry:

    def __init__(self, id_num, name, last_name, phone_nr):
        self.id_num = id_num
        self.name = name
        self.last_name = last_name
        self.phone_nr = phone_nr

                        # ****************** NEW ENTRY FUNCTION *******************
    @staticmethod
    def new():
        while True:
            print('In order to create new Phone Book record, please enter required data.')
            id_num = input('ID Number: ')
            name = input('Name: ')
            last_name = input('Last Name: ')
            phone_number = input('Phone Number: ')
            print('New entry has been successfully added!')
            print('New entry data is Name: {}, Last Name: {}, Phone Number: {}'.format(name, last_name, phone_number))
            return Entry(id_num, name, last_name, phone_number)

    # @staticmethod
    def edit_entry(self):
        while True:
            print('In order to Edit a PhoneBook record, please enter required data.')
            entered_id = input('Please, enter ID of an entry you want to change.')
            if entered_id:
                name = input('Name: ')
                last_name = input('Last Name: ')
                phone_number = input('Phone Number: ')
                print('Data has been successfully changed!')
                return Entry(name, last_name, phone_number)



                                        #************ EDIT LOOP **********
    # def edit(self):
        #petla do edytowania wpisu


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
        Entry.edit_entry()

    elif chosen_menu_option == 3:
        print('\nHere you\'ll see "browse()" function')
        #TODO creat browse() method


    elif chosen_menu_option == 4:
        print('\nThe PhoneBook has ended. Thanks and see you next time!')
        break
