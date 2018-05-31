price_box=[]
for i in range(10000):
    while True:
        try:
            price=float(input("Product Price "+str(i+1)+" :"))
            break
        except ValueError:
            print("Please Enter a Numeric Value")
    
    
    price_box.append(float(price))
total=sum(price_box)
if total >5000 :
    discount = 12
elif total > 3000 :
    discount = 10
elif 3000>total >1000 :
    discount = 5
elif total <1000 :
    discount = 0
dis=total*discount/100.0
net_price=total-dis
text_file=open(" SavedData.txt" ,  "w")
text_file.write(" Item Price: %s" % price_box )
text_file.write(" Discount Precentage: %s" % discount )
text_file.write(" Saved Price: %s" % dis )
text_file.close()
print("\n\nNet Price = Rs.",net_price)
