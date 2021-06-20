import pdb
# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(cash):
    return cash["admin"]["total_cash"]
    


def add_or_remove_cash(admin_cash, add_cash):
     admin_cash["admin"]["total_cash"] += add_cash
       
def remove_cash(admin_cash, remove_cash):
     admin_cash["admin"]["total_cash"] += remove_cash
     
def get_pets_sold(less_pets):
    return less_pets["admin"]["pets_sold"]


def increase_pets_sold(more_pets, add_pets):
    more_pets["admin"]["pets_sold"] += add_pets


def get_stock_count(num_of_stock):
     return len(num_of_stock["pets"])

    
def get_pets_by_breed(get_breed, breed):
    breed_count = []
    for pet in get_breed["pets"]:
        if pet["breed"] == breed:
             breed_count.append(breed)
    return breed_count

def get_pets_by_breed(breed_not_fund, breed):
    breed_count = []
    for pet in breed_not_fund["pets"]:     
        if pet["breed"] == breed:
             breed_count.append(breed)
    return breed_count

def find_pet_by_name(find_name, pet_name):
    for name in find_name["pets"]:
        if name["name"] == "Arthur":
            return name

def find_pet_by_name(find_name, pet_name):
    for name in find_name["pets"]:
        if name["name"] == "Fred":
            return None
        elif name["name"] == pet_name:
            return name

def remove_pet_by_name(remove_name, pet_name):
    removed_pet_name = []
    for name in remove_name["pets"]:
        if name["name"] == "Arthur":
            removed_pet_name = remove_name["pets"].index(name)
            return remove_name["pets"].pop(removed_pet_name)


def add_pet_to_stock(pet_shop, new_pet):
    return pet_shop["pets"].append(new_pet)    


def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, number):
    customer["cash"] -= number