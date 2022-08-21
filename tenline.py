import qrcode
"""
Here is the code that make the qr code
cutting the middle man out. 
I have obtain this solution by going through the internet 
"""
# the link that you want to make it go to, belongs in what is in the "" 
img= qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSepdVgljkuT8sdFMGrsl6XNOZVYuMwp2RoUDwHrs7Ckzpj4bg/viewform?vc=0&c=0&w=1&flr=0")
# here is the name that you want to call the QR Code
img.save("NombreCompleto.jpg")
