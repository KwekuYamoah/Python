# A simple program that prints the encoded version of a message in Uni-code
def m_encoded():
    mess = input("Enter thy message:")
    encoded = []
    print("Encoding is :")
    for x in mess:
        encoded.append(x)
        for i in encoded:
            p= ord(i)
        print(str(p),end="")






def m_decoded():
        dec_1= int(input("Enter first character \n"))
        dec_2= int(input("Enter second character \n"))
        dec_3= int(input("Enter third character \n"))
        dec_4= int(input("Enter fourth character \n"))
        dec_5= int(input("Enter fifth character \n"))
        print("Your message:" + chr(dec_1),chr(dec_2),chr(dec_3),chr(dec_4),chr(dec_1))

m_decoded()   
              
        
