tasks = [{"name": "break fast", "is_completed" : False},{"name": "Go bath","is_completed":True}]


while True:
  print('\n\n ===============SIMPLE TODO APPLICATION===========')

  print("1.View all task")

  print("2.Add Task")  
  print("3.Delete") 
  print("4.Mark task as completed")
  print("0.Quit")
  print("------------")

  choice = int(input("Choose from the above list: "))


  if choice ==1:
   print("\n Your added tasks: ")
   for index,task in enumerate(tasks):
    print(f'{index+1}:{task["name"]}-{task["is_completed"]}')

  elif choice ==2:
   value = input("Enter task: ")
   newTask = {'name':value, "is_comleted":False}
   tasks.append(newTask)
   print("\n----Task is added successfully-----")

   for index,task in enumerate(tasks):
    print(f'{index+1}:{task["name"]}')

  elif choice == 3:
   delTask = int(input("Enter task index to delete: "))
   tasks.pop(delTask-1)

   print("\n-------Task deleted successfully------")

  elif choice == 4:
   markPosition = int(input("Enter the task to mark complete: "))
   tasks[markPosition-1]["is_completed"] = True
   print("----Marked as completed----")


  elif choice ==0:
    print("Good bye")
    break

"""
inventry ={ "one":1, "two":2,"three":3}
inventry["banana"] =7
print(inventry)
inventry.update({'banana':5,"grapes":100})
print(inventry)
# inventry.pop("banana")
# print(inventry)
# inventry.popitem()
# inventry.clear()
print("apple" not in (inventry))
print(inventry.keys())
print(inventry.values())"""