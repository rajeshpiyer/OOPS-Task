class Restaurant_Bill:
    parcel_charge = 20

    def __init__(self, price1,price2,price3):
        self.price1 = price1
        self.price2 = price2
        self.price3 = price3

    def gross_price(self):
        return self.price1 + self.price2 + self.price3

    @classmethod
    def total_price(cls,gross_price):
        return gross_price + cls.parcel_charge

    @staticmethod
    def net_price(total_price):
        gst = total_price * 0.018
        return gst, total_price + gst

print("Enter Prices : ")
price1 = int(input("Item 1 : "))
price2 = int(input("Item 1 : "))
price3 = int(input("Item 1 : "))
bill1 = Restaurant_Bill(price1,price2,price3)
gross_price = bill1.gross_price()
total_price = bill1.total_price(gross_price)
gst,net_price = Restaurant_Bill.net_price(total_price)

print("\n\n---------- BILL ------------\nParticulars\tAmount\n")
print(f"Item 1\t\t{price1}\nItem 2\t\t{price2}\nItem 3\t\t{price3}\nParcel charges\t{Restaurant_Bill.parcel_charge}")
print("----------------------------")
print(f"Total\t\t{total_price}")
print(f"+GST\t\t{gst}")
print("----------------------------")
print(f"Net Payable\t{net_price}")
print("----------------------------\n\n")