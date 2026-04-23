#bank 
#customer
#name
#create account
#deposit
#check balance


#structure for saving data
"""
{'customerID' :{data}}
{'1234nnnn': {'name':'indira', 'balence':0}}
"""


class Bank:


  #geting name as input for the bank account 
  def __init__(self,name):
    self.name = name
    #an dict to store the customers
    self.customers = {}


  #creating customers for bank and getting the data as arguments

  def create_customer(self,coustomer_id,name,initial_balence=0):
    
    #adding customer values to the empty dict and adding the data as a dict inside a dict
    self.customers[coustomer_id] = {
      "name": name,
      "balance": initial_balence
    }

  def view_customers(self):
    for i in self.customers:
      print(f"{i}. Name: {self.customers[i]["name"]}, Balence:{self.customers[i]["balance"]}")


  def deposite(self,customer_id,amount):

    customer = self.customers[customer_id]
    customer["balance"] += amount

    print(f"{amount} sucessfully added to {self.customers[customer_id]["name"]}\ncurrent balance is {customer["balance"]}")
  
  def withdraw(self,customer_id,amount):
    customer = self.customers[customer_id]
    customer["balance"] -= amount

    print(f"{amount} is sucessfully debited from {self.customers[customer_id]["name"]} \ncurrent balance is {customer["balance"]} ")


  def check_balence(self,customerId):
    customer = self.customers[customerId]
    print(f"{customer["name"]} your current balance is {customer["balance"]}")


my_bank = Bank("Indian Bank")

my_bank.create_customer("A0001","indira")
my_bank.deposite("A0001",10000000)
my_bank.withdraw("A0001",1)
my_bank.create_customer("A0002","pavakka")

my_bank.view_customers()
my_bank.check_balence("A0001")
