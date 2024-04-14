inventory={}
class Inventory:
    def __init__(self,name,quantity,price):
      
        self.name=name
        self.quantity=quantity
        self.price=price
        # self.new_quantity=new_quantity

def addItem(name,quantity,price):
    item= Inventory(name,quantity,price)
    inventory[name]=item

def UpdateQuantity(name,new_quantity):

    if name in inventory:
        inventory[name].quantity = new_quantity  
        print(new_quantity)
    else:
        print(f'{name} not found')


def UpdatePrice(name,new_price):
    if name in inventory:
        inventory[name].price = new_price 
        print(new_price)
    else:
        print(f'{name} not found')

def DeleteItem(del_item):
    if del_item in inventory:
        inventory.pop(del_item)
    else:
        print(f'{del_item} is not found Hence it cannot be deleted')

def SellItem(Item_name,desired_quantity):
    if Item_name in inventory:
        if desired_quantity>=inventory[Item_name].quantity:
            print("insufficient quantity in the inventory")
        else:
            inventory[Item_name].quantity-=desired_quantity
            print(f'{desired_quantity} units of {Item_name} sold.')
    else:
        print(f'{Item_name} not found in the inventory')

def RestockItem(restock_item,Restock_quantity):
    if restock_item in inventory:
       
            inventory[restock_item].quantity+=Restock_quantity
            print(f'{Restock_quantity} units of {restock_item} added.')

    else:
        print(f'{restock_item} not found in the inventory')


        
def DisplayInventory():
    
    for name,item in inventory.items():
     
        print(f' Name: {item.name}, Quantity: {item.quantity}, Price: ${item.price}')

def SearchItem(Searchitem):
    if Searchitem in inventory:
        print(f'{Searchitem} IS AVAILABLE in the inventory')
    
    else:
        print(f'{Searchitem}, is NOT AVAILABLE in the inventory')

# total value of the inventory based on the quantity and price of each item. This can provide insights into the overall worth of the inventory.

def Tot_val_inventory_based_quantity_and_price(itemName):
    if itemName in inventory:
        tot_price = inventory[itemName].quantity*inventory[itemName].price  
        print(f'{tot_price}Rs of {itemName} stock available in the Inventory')
    else:
        print(f'{itemName} is not found')

def main():
  
    while True:
        print("\nInventory Management System\n")
        print("1. Add Item")
        print("2. Update Quantity")
        print("3. Update Price")
        print("4. Delete Item")
        print("5. Sell Item")
        print("6. Restock Item")
        print("7. Display Inventory")
        print("8. search item")
        print("9. Tot_val_inventory_based_quantity_and_price")
        print("10. Exit")

        choice=input("Input your choice :")

        if choice=='1' :
            name=input("input name of the product : ")
            quantity=float(input("Enter quantity: "))
            price=int(input("input price of the product : "))
            addItem(name,quantity,price)

        elif choice=='2':
            name=input("Enter the name of the item : ")
            new_quantity=float(input("Input the new quantity : "))

            UpdateQuantity(name,new_quantity)

        elif choice=='3':
            name=input("Enter the name of the item : ")
            new_price=int(input("Input the new Price : "))

            UpdatePrice(name,new_price)

        elif choice=='4':
            del_item=input("Enter the item to be deleted : ")
            DeleteItem(del_item)

        elif choice=='5':
            Item_name=input("Enter item name : ")
            desired_quantity=float(input("Input required quantity : "))
            SellItem(Item_name,desired_quantity)

        elif choice=='6':
            restock_name=input("Enter the stock to be Restored : ")
            Restock_quantity=float(input("Input the Restock quantity : "))
            RestockItem(restock_name,Restock_quantity)

        elif choice=='7':
            DisplayInventory()

        elif choice=='8':
            Searchitem=input("Enter the name of the item to be searched : ")
            SearchItem(Searchitem)

        elif choice=='9':
            itemName=input("Enter the item :")
            Tot_val_inventory_based_quantity_and_price(itemName)

        elif choice=='10':
            break
            
main()