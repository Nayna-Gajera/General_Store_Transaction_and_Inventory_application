import xlrd
from xlutils.copy import copy


class Inventory:
    def __init__(self, id, p_name, price, qty, discount):
        self.id = id
        self.p_name = p_name
        self.price = price
        self.qty = qty
        self.discount = discount


location = xlrd.open_workbook(r'C:\Users\018810569\List_Of_Product.xls')
sheet_1 = location.sheet_by_index(0)
sheet_2 = location.sheet_by_index(1)
wb = copy(location)
w_sheet = wb.get_sheet(0)
inv_list = []
for i in range(1, sheet_1.nrows):
    for j in range(1, sheet_2.nrows):
        if int(sheet_1.cell_value(i, 0)) == int(sheet_2.cell_value(j, 0)):
            discount = int(sheet_2.cell_value(j, 1))
            break

    inv = Inventory(int(sheet_1.cell_value(i, 0)), sheet_1.cell_value(i, 1), int(sheet_1.cell_value(i, 2)),
                    int(sheet_1.cell_value(i, 3)), discount)  # we created object which stores all values
    inv_list.append(inv)

# for invObj in inv_list:
# print(invObj.id, invObj.p_name, invObj.price, invObj.qty)
for i in range(sheet_1.nrows):
    print(sheet_1.row_values(i))

total = 0
while True:
    product_id = int(input("\nEnter product ID you want to buy: "))
    quantity = int(input("Enter number of quantity you want to buy: "))
    count = 1
    for invObj in inv_list:
        if product_id == invObj.id:
            if quantity > invObj.qty:
                print("sorry we only have", invObj.qty, "quantity of", invObj.p_name)
            else:
                sum = quantity * invObj.price
                sum = sum - (sum*(invObj.discount/100))
                total = total + sum
                invObj.qty = invObj.qty - quantity
                w_sheet.write(count, 3, invObj.qty)
        count += 1
    wb.save(r'C:\Users\018810569\List_Of_Product.xls')

    while True:
        choice = str(input("\nDo you want to buy more? Please enter Yes or No: "))
        if choice == "No".casefold() or choice == "yes".casefold():
            break
        else:
            print('\nPlease enter valid choice either "Yes" or "No"!!!')

    if choice == "No".casefold():
        break

membership = str(input('Do you have membership? Please enter "Yes" or "No: '))
if membership == "yes".casefold():
    total = total * 0.8
    print(total)
elif membership == "No".casefold():
    print(total)
else:
    print('\nPlease enter valid choice either "Yes" or "No"!!!')
