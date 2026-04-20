#contact manager 

'''
tasks:
add(name phone email)
view
remove
search


'''



#lets take an list of dictionaries to store all the data

contacts = [
  {"name":"Tamil", "phone":"1554782645", "email":"tamil@gamilcom"},

  {"name":"Indira","phone":"5874695438","email":"indira@gamil.com"},
  
  {"name":"pavakka","phone":"7894568742","email":"pavakka@gmail.com"}
]


while True :
  print("\n=====CONTACT MANAGER=====")
  print("0.Exit")
  print("1.Display contacts")
  print("2.Add new contact")
  print("3.Remove contact")
  print("4.Search contact")

  choice = int(input("\nEnter choice : "))


  if choice ==1:
    if not contacts:
      print("No contacts found")
    else:
      for index, item in enumerate(contacts):
        print(f"({index+1}) Name: {item["name"]}, Email: {item["email"]}, Phone: {item["phone"]}") 
  elif choice ==2:
    newName =input("Enter name: ").strip()
    newPhone = input("Enter phone number: ").strip()
    newEmail = input("Enter email: ").strip()

    newContact = {"name":newName, "email":newEmail, "phone":newPhone}

    contacts.append(newContact)

    print(f"{newName} added successfully.")
  elif choice == 4:
    searchName = input("Enter name:").strip()
    is_found = False
    for index,item in enumerate(contacts) :
      
      if item["name"].lower()== searchName.lower():
        print(f"Name: {item["name"]}, Email: {item["email"]}, Phone: {item["phone"]} ")
        is_found = True
    else:
      if is_found == False :    
        print("No contact found:( ")
  
  elif choice == 3:
    delName = input("Enter name to delete: ").strip()

    for index,item in enumerate(contacts):
      if delName.lower() == item["name"].lower():
        id = index
        contacts.pop(index)
        print("Contact deleted successfully...")



  elif choice ==0:
    print("Good byeee")
    break
