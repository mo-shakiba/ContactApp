import re

""" This is a class for implementing the following methods:
1. Get all the information about the contact back > def data
2. Add a contact > def new
3. Remove a contact > def remove
4. Change the information of a contact > def alter
5. Search for a contact > def find
6. Get the information of a contact back > def retrieve
7. Count how much a contact has been searched > def count
8. Retrieve the count > def get_count
9. Sort contacts > def sorter
"""


class Contact:
    def __init__(
        self, Fnames=[], Lnames=[], Numbers=[], City=[], Kinds=[], Desc=[], Count=[]
    ):
        # initializing the lists
        self.Fnames = Fnames
        self.Lnames = Lnames
        self.Numbers = Numbers
        self.City = City
        self.Kinds = Kinds
        self.Desc = Desc
        self.Count = Count

    def data(self):
        # returning all the information stored in the lists
        return self.Fnames, self.Lnames, self.Numbers, self.City, self.Kinds, self.Desc

    def new(self, first, last, number, city, kind, desc=""):
        # adding a new contact by appending inputs to the corresponding lists
        self.Fnames.append(first)
        self.Lnames.append(last)
        self.Numbers.append(number)
        self.City.append(city)
        self.Kinds.append(kind)
        self.Desc.append(desc)
        self.Count.append(0)

    def remove(self, i):
        # removing a contact from the list by index
        self.Fnames.pop(i)
        self.Lnames.pop(i)
        self.Numbers.pop(i)
        self.City.pop(i)
        self.Kinds.pop(i)
        self.Desc.pop(i)

    def alter(self, i, first, last, number, city, kind, desc):
        # replacing an item in the list by first checking that the value wants to be changed
        if first != "":
            self.Fnames[i] = first
        if last != "":
            self.Lnames[i] = last
        if number != "":
            self.Numbers[i] = number
        if city != "":
            self.City[i] = city
        if kind != "":
            self.Kinds[i] = kind
        if desc != "":
            self.Desc[i] = desc

    def find(self, first, last):
        # using regex to match the input to the lists and returning the index
        if first != "":
            for i, s in enumerate(self.Fnames):
                if re.match(first, s):
                    return i
        if last != "":
            for i, s in enumerate(self.Lnames):
                if re.match(last, s):
                    return i
        return None

    def retrieve(self, i):
        # using the index to retrieve the information about a specific contact
        return self.Fnames[i], self.Lnames[i], self.Numbers[i]

    def count(self, i):
        # increasing the value of 0 by 1 if the contact has been searched
        self.Count[i] = self.Count[i] + 1

    def get_count(self, i):
        # getting the count number of a specific contact back
        return self.Count[i]

    def sorter(self, based):
        # intializing a list and sorting by First | Last | Number
        # saving the index value of a sorted list in 'lst'
        # using the indexes later to sort all the lists
        lst = []
        if based == "First":
            sortF = self.Fnames.copy()
            sortF.sort()
            for i in sortF:
                # j is the index, n is the member of the list
                # finding the index of i in the original list
                for j, n in enumerate(self.Fnames):
                    if i == n:
                        lst.append(j)
            return self.Fnames, self.Lnames, self.Numbers, lst
        elif based == "Last":
            sortL = self.Lnames.copy()
            sortL.sort()
            for i in sortL:
                for j, n in enumerate(self.Lnames):
                    if i == n:
                        lst.append(j)
            return self.Lnames, self.Fnames, self.Numbers, lst
        elif based == "Number":
            sortN = self.Numbers.copy()
            sortN.sort()
            for i in sortN:
                for j, n in enumerate(self.Numbers):
                    if i == n:
                        lst.append(j)
            return self.Numbers, self.Fnames, self.Lnames, lst


def main():
    """
    Prompts the user for a number from the menu
    Uses condition to call a function
    """
    while True:
        print("****** MENU ******")
        print("0 - All")
        print("1 - add")
        print("2 - delete")
        print("3 - change")
        print("4 - search")
        print("5 - search count")
        print("6 - sort")
        print("******************")
        query = input("Select: ")
        if query == "0":
            All()
        elif query == "1":
            add()
        elif query == "2":
            delete()
        elif query == "3":
            change()
        elif query == "4":
            search()
        elif query == "5":
            search_c()
        elif query == "6":
            sort()
        # just to promot for an enter to continue
        pause = input("Press Enter")


def All():
    # gets all the data in contact back and print them
    f, l, n, c, k, d = contact.data()
    for _ in range(len(f)):
        print(_, f[_], l[_], n[_], c[_], k[_], d[_])


def add():
    # prompts for all the options
    # uses the method .new() for the object contact
    f = input("First Name: ")
    l = input("Last Name: ")
    n = input("Number: ")
    c = input("City: ")
    k = input("Mobile | Home | Work: ")
    d = input("Description: ")
    contact.new(f, l, n, c, k, d)
    print("----------------------------")
    print("Contact Added :)")
    print("----------------------------")


def delete():
    # shows all contacts
    All()
    # prompts for the index of a contact in the list
    i = int(input("Index: "))
    # uses the method .remove() for the object contact
    try:
        contact.remove(i)
    # if the index is out of range: error message
    except:
        print("Couldn't Delete :(")
    else:
        print("----------------------------")
        print("Contact Deleted :) ")
        print("----------------------------")


def change():
    # shows all contacts
    All()
    # prompts for the index of a contact in the list
    i = int(input("Index: "))
    # prompts for all the options
    fn = input("New First Name: ")
    ln = input("New Last Name: ")
    nn = input("New Number: ")
    cn = input("New City: ")
    kn = input("New Mobile | Home | Work: ")
    dn = input("New Description: ")
    # uses the method .alter() for the object contact
    try:
        contact.alter(i, fn, ln, nn, cn, kn, dn)
    # if the index is out of range : error message
    except:
        print("Couldn't Change :(")
    else:
        print("----------------------------")
        print("Contact Changed :)")
        print("----------------------------")


def search():
    # prompts for all the options
    fs = input("First Name to search: ")
    ls = input("Last Name to search: ")
    # uses the method .find() for the object contact
    i = contact.find(fs, ls)
    # if i has a value > found the contact
    if i != None:
        # uses the method .retrieve() for the object contact
        first, last, number = contact.retrieve(i)
        # uses the method .count() for the object contact
        contact.count(i)
        print("----------------------------")
        print("Found > ", first, last, number)
        print("----------------------------")
    else:
        print("Contact Not Found :(")


def search_c():
    # shows all contacts
    All()
    # prompts for the index of a contact in the list
    i = int(input("Index: "))
    # uses the method .get_count() for the object contact
    try:
        count = contact.get_count(i)
    # if the index is out of range : error message
    except:
        print("Index out of range :(")
    else:
        print("----------------------------")
        print(f"Searched: {count} time(s)")
        print("----------------------------")


def sort():
    # prompts for all the options
    print("#### Select one to sort ####")
    # gets sorting preference
    b = input("First | Last | Number: ")
    # uses the method .sorter() for the object contact
    try:
        A, B, C, L = contact.sorter(b)
    # if b does not equal First | Last | Number > error message
    except:
        print("Invalid sort request")
    else:
        print("----------------------------")
        for j in L:
            print(A[j], B[j], C[j])
        print(f"Sorted by: {b}")
        print("----------------------------")


if __name__ == "__main__":
    # making a Contact object
    contact = Contact()
    main()
