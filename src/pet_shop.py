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





    

 
