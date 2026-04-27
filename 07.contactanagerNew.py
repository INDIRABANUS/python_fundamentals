#contact manager 

'''
tasks:
add(name phone email)
view
remove
search
'''


class ContactManager:
  def __init__(self):
    self.contacts = [{"name":"Tamil", "number":"1554782645", "mail":"tamil@gamilcom"},

                    {"name":"Indira","number":"5874695438","mail":"indira@gamil.com"},
                    
                    {"name":"pavakka","number":"7894568742","mail":"pavakka@gmail.com"}]


  

  

  def add_contact(self):
    number = input("Enter number: ")
    name = input("Enter name: ")
    mail = input("Enter mail: ")
   

    contact = {"name":name,"number":number,"mail":mail}

    self.contacts.append(contact)

    print(f"\n{name} added successfully!")

  def view_contact(self):
    for index,item in enumerate(self.contacts):
      print(f"ID:{index+1}, Name:{item["name"]}, Number:{item["number"]}, Mail:{item["mail"]}")
    print("\n")

  def remove_contact(self):
    removeId = int(input("Enter contact id to remove: "))
    
    for index,item in enumerate(self.contacts):
      if removeId == index+1:
        self.contacts.remove(item)
        
        print(f"{item["name"]} is removed :)")

  def search_contact(self):
    search_name = input("Enter name: ")
    found = False 

    for index,item in enumerate(self.contacts):
    
      if item["name"].lower() == search_name.lower():
        print(f"ID:{index+1}, Name:{item["name"]}, Number:{item["number"]}, Mail:{item["mail"]}")
        found = True
    else:
      if found == False:
        print("Invalid")

        



my_book = ContactManager()

while True:
  print("\n===CONTACT MANAGER===")

  print("1. Add contact")
  print("2. View all contact")
  print("3. Remove contact")
  print("4. Search contact")
  print("5. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    my_book.add_contact()

  elif choice == 2:
    my_book.view_contact()

  elif choice == 3:
    my_book.remove_contact()

  elif choice == 4:
    my_book.search_contact()

  elif choice == 0:
    print("Thank you")
    break
    


