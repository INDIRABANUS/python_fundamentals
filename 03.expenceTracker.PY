#EXPENCE TRCKER
#ADD EXPENCE
#VIEW MONTHLY SALARY
#FILTER EXPENSE BASED ON CATEGORY
#DELETE EXPENCE


expence = []

def save_in_file():
  with open("expence.txt","w") as file:    
    for index,item in enumerate(expence):
      file.write(f"\n ({index}) {item["amount"]},{item["catogory"]},{item["date"]}")

def update_exsisting_record():
  with open("expence.txt","r") as file:
    for line in file:
      separated_values = line.strip().split(',')
      item = {"amount":separated_values[0],"catogory": separated_values[1],"date":separated_values[2]}
      expence.append(item)


update_exsisting_record()



while True:
  print("\n=== EXPENCE TRACKER ===")
  print("1. Add expence")
  print("2. View all expence")
  print("3. Filter expence based on catogory")
  print("4. monthly average")
  print("5. Delete expense")
  print("0. Exit")

  choice= int(input("Choose an option from the above : "))

  if choice == 1:
    amount = input("Enter amount: ")
    catogory = input("Enter catogory: ").strip()
    date = input("Enter date in dd-mm-yyyy formate: ")
    newExpence = {"amount":amount, "catogory":catogory, "date":date}
    expence.append(newExpence)
    save_in_file()
    print(f"{amount} added successfully:)")

    


  elif choice == 2:
    if not expence:
      print("Expences not found")
    else:
      for index, item in enumerate(expence):
        print(f"Amount: {item["amount"]}, Catogory: {item["catogory"]}, Date: {item["date"]}\n")

  elif choice == 3:
    #filter based on catogory
    search_catogory = input("Enter Catogory: ")
    catagoryTotal = 0
    for index ,item in enumerate(expence):
      cat = item["catogory"]
      if search_catogory.lower() == cat.lower():
        print(f"\n({index+1}) Amount: {item["amount"]}, Catogory: {item["catogory"]}, Date: {item["date"]}")

        catagoryTotal += int(item["amount"])
      else:
        ("No result found")
    print(f"\n Catagory total is {catagoryTotal}")

  elif choice == 4:
    #monthly average
    input_month = input("Enter the month for average in mm-yyyy formate: ")

    monthTotal = 0

    for item in expence:
      if item["date"].endswith(input_month):
        monthTotal += int(item["amount"])
    print(f"\n{input_month} total expense is {monthTotal}")

  elif choice == 5:
    #deleting

    delete_input = int(input("Enter index to delete: "))-1
    print(f"\n {expence[delete_input]["amount"]} Deleted successfully")
    expence.pop(delete_input)

    save_in_file()
    


  elif choice == 0:
    print("Good byeee")
    break