from datetime import datetime

def save_data(product_ok, product_ng):
    file = open("product\\text.txt",'r+')
    file.write("\n" + datetime.now().strftime("%A %d %B %Y %I:%M:%S%p ") + "Product_OK:" +str(product_ok))
    file.write("\n" + datetime.now().strftime("%A %d %B %Y %I:%M:%S%p ") + "Product_NG:"+ str(product_ng))
    file.close()

def read_data():
    file = open("product\\text.txt", 'r+')
    line = file.read(100)
    print("Read Lines: %s" % (line))
    file.close()