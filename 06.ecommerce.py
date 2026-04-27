#ECOMMERCE WEB


# admin login 
# admin create products 
# user login 
# user view products 
# user add products to cart 
# user make orders


"""product structure [{id:1, name:"apple",price:100},
                      {id:2, name:"orange",price:200},
]

"""
#creating class ---  first letter should be in upper case

class Ecommerce:

  def __init__(self):
    self.is_admin_logined = False
    self.product_id = 0     
    self.products = []
  
  def login_admin(self):

    email = input("Enter your email: ")

    password = input("Enter password: ")

    if email == "admin@mail.com" and password == "password":
      self.is_admin_logined = True  
    else:
      print("Invalid please try again.") 


  def create_product(self):
    product_name = input("Enter product name: ")
    product_price = input ("Enter the product price: ")
    self.product_id += 1


    product = {"id":self.product_id, "name":product_name, "price":product_price}

    self.products.append(product) 

    print(f"{product_name} added succesfully")

  def render_product(self):
    for i in self.products:
      print(f"{i["id"]}. Name:{i["name"]} , Price:{i["price"]} ")



my_commerce = Ecommerce()

while True:
  print("\n===ECOMMERCE APPLICTION===")

  if my_commerce.is_admin_logined:
    print("1. Create product")
    print("2. view product")
    print("3. Exit")

    choice = int(input("Enter a choice: "))

    if choice == 1:
      my_commerce.create_product()

    elif choice == 2:
      my_commerce.render_product()
    elif choice == 3:
      print("Thank you")
      break

  else:
      role = input("DO you want to login admin? (yes/no) : ")

      if role == "yes":
        my_commerce.login_admin()
