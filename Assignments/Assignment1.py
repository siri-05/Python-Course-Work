productID=int(input("Enter Product ID: "))
productName=input("Enter Product Name: ")
price=float(input("Enter Price: "))
categories=input("Enter Categories(comma-separated): ").split(',')
stockDetails=(int(input("Enter Available Stock: ")),int(input("Enter Sold Stock: ")))
discount=float(input("Enter Discount Percentage: "))
productFeatures=set(input("Enter Product Features(comma-separated): ").split(','))
supplierDetails={"Name":input("Enter Supplier Name: "),"Contact":input("Enter Supplier Contact Number: "),"Location":input("Enter Supplier Location: ")}

print("Product ID, Name, Price: ",productID,", ",productName,", ",price)
print("Product Discount : %0.2f"%discount,"%")
print(f"Product Name: {productName}\nPrice: ₹{price}\nDiscount: {discount}%\nStock Available: {stockDetails[0]} units")
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(supplierDetails["Name"],supplierDetails["Contact"],supplierDetails["Location"]))