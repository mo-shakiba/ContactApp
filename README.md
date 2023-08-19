<h1 id="ContactApp">ContactApp</h1>
<p><hr></p>
<h4 id="abikahs">M. H. Shakiba</h4>
<hr> 

##### 1. Importing re library.
later on we will use regex to implenent search method.


```python
import re
```

##### 2. Constructing a Class Object.
Here we construct a class to implement our desired methods.

##### 2.1 **init**
initalizing the necessary lists to be used later.


```python
class Contact():
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
```

##### 2.2 **data**
this function is implemented to retrieve all the contacts.


```python
class Contact(Contact):
        def data(self):
            # returning all the information stored in the lists
            return self.Fnames, self.Lnames, self.Numbers, self.City, self.Kinds, self.Desc
```

##### 2.3 **new**
this function is implemented to add a new contact to the list.


```python
class Contact(Contact):
    def new(self, first, last, number, city, kind, desc=""):
        # adding a new contact by appending inputs to the corresponding lists
        self.Fnames.append(first)
        self.Lnames.append(last)
        self.Numbers.append(number)
        self.City.append(city)
        self.Kinds.append(kind)
        self.Desc.append(desc)
        self.Count.append(0)
```

##### 2.4 **remove**
this function is implemented to remove a contact from the list.


```python
class Contact(Contact):
    def remove(self, i):
        # removing a contact from the list by index
        self.Fnames.pop(i)
        self.Lnames.pop(i)
        self.Numbers.pop(i)
        self.City.pop(i)
        self.Kinds.pop(i)
        self.Desc.pop(i)
```

##### 2.5 **alter**
this function is implemented to change a contact in the list.


```python
class Contact(Contact):
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
```

##### 2.6 **find**
this function is implemented to search for a contact in the list.


```python
class Contact(Contact):
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
```

##### 2.7 **retrieve**
this function is implemented to retrieve the information about a specific contact.


```python
class Contact(Contact):
    def retrieve(self, i):
        # using the index to retrieve the information about a specific contact
        return self.Fnames[i], self.Lnames[i], self.Numbers[i]
```

##### 2.8 **count and get_count**
these functions are implemented to count the amount of times a contact has been searched.


```python
class Contact(Contact):
    def count(self, i):
        # increasing the value of 0 by 1 if the contact has been searched
        self.Count[i] = self.Count[i] + 1

    def get_count(self, i):
        # getting the count number of a specific contact back
        return self.Count[i]
```

##### 2.9 **sorter**
these functions is used to sort contacts by First, Last or Phone Numbers.


```python
class Contact(Contact):
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
```

##### 3 Implementing main()
Showing a menu and prompting the user for input.


```python
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
```

##### 3.0 **All**


```python
def All():
    # gets all the data in contact back and print them
    f, l, n, c, k, d = contact.data()
    for _ in range(len(f)):
        print(_, f[_], l[_], n[_], c[_], k[_], d[_])
```

##### 3.1 **add**


```python
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
```

##### 3.2 **delete**


```python
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
```

##### 3.3 **change**


```python
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
```

##### 3.4 **search**


```python
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
```

##### 3.5 **search_c**


```python
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
```

##### 3.6 **sort**


```python
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
```

##### 4. Program execution
calling the main() function


```python
if __name__ == "__main__":
    # making a Contact object
    contact = Contact()
    main()
```
<hr>
