# ContactApp

ContactApp is a simple Python application for managing and organizing your contacts. This documentation provides a comprehensive guide on how to use ContactApp effectively.

## Table of Contents
1. [Getting Started](#getting-started)
    1. [Importing the `re` Library](#importing-re-library)
    2. [Constructing a Class Object](#constructing-class-object)
2. [Contact Management](#contact-management)
    1. [Adding a New Contact](#adding-new-contact)
    2. [Removing a Contact](#removing-contact)
    3. [Changing Contact Information](#changing-contact-information)
    4. [Searching for a Contact](#searching-for-contact)
    5. [Counting Contact Searches](#counting-contact-searches)
    6. [Sorting Contacts](#sorting-contacts)
3. [Program Execution](#program-execution)

## 1. Getting Started <a id="getting-started"></a>

### 1.1 Importing the `re` Library <a id="importing-re-library"></a>

Before using the ContactApp, ensure you import the `re` library for regular expression support. This is essential for implementing the search method.

```python
import re
```

### 1.2 Constructing a Class Object <a id="constructing-class-object"></a>

To use the ContactApp, create an instance of the `Contact` class. This class provides methods for managing your contacts.

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

## 2. Contact Management <a id="contact-management"></a>

### 2.1 Adding a New Contact <a id="adding-new-contact"></a>

You can add a new contact using the `new` method, providing details such as first name, last name, phone number, city, contact type (e.g., Mobile, Home, Work), and an optional description.

```python
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

### 2.2 Removing a Contact <a id="removing-contact"></a>

To remove a contact, use the `remove` method and provide the index of the contact you wish to delete.

```python
def remove(self, i):
    # removing a contact from the list by index
    self.Fnames.pop(i)
    self.Lnames.pop(i)
    self.Numbers.pop(i)
    self.City.pop(i)
    self.Kinds.pop(i)
    self.Desc.pop(i)
```

### 2.3 Changing Contact Information <a id="changing-contact-information"></a>

Use the `alter` method to modify the details of an existing contact. Specify the index of the contact you want to change and provide new information for each field.

```python
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

### 2.4 Searching for a Contact <a id="searching-for-contact"></a>

To search for a contact, use the `find` method. Provide either the first name or last name as search criteria, and it will return the index of the first matching contact.

```python
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

### 2.5 Counting Contact Searches <a id="counting-contact-searches"></a>

You can keep track of how many times you've searched for a contact using the `count` and `get_count` methods. The `count` method increments the search count for a contact, while `get_count` retrieves the count.

```python
def count(self, i):
    # increasing the value of 0 by 1 if the contact has been searched
    self.Count[i] = self.Count[i] + 1

def get_count(self, i):
    # getting the count number of a specific contact back
    return self.Count[i]
```

### 2.6 Sorting Contacts <a id="sorting-contacts"></a>

You can sort your contacts by first name, last name, or phone number using the `sorter` method. Specify your sorting preference as "First," "Last," or "Number." It returns the sorted lists of contacts along with the indexes for reference.

```python
def sorter(self, based):
    # initializing a list and sorting by First | Last | Number
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

## 3. Program Execution <a id="program-execution"></a>

To use the ContactApp, call the `main` function. This function displays a menu to interact with the application.

```python
def main():
    """
    Prompts the user for a number from the menu


    Uses condition to call a function
    """
    while True:
        print("****** MENU ******")
        print("0 - All")
        print("1 - Add")
        print("2 - Delete")
        print("3 - Change")
        print("4 - Search")
        print("5 - Search Count")
        print("6 - Sort")
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
        # just to prompt for an enter to continue
        pause = input("Press Enter")

if __name__ == "__main__":
    # making a Contact object
    contact = Contact()
    main()
```
