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

def find_pet_by_name(find_name, b):
    for name in find_name["pets"]:
        if name["name"] == "Arthur":
            return name
