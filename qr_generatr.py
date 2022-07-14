#qrcode generator program black and white formet


import qrcode as qr
# img = qr.make("https://www.youtube.com/")   # Write any link as you want
# img.save("you.png")
  
  
  #qrcode generator program in formaated form 
from PIL import Image
qro = qr.QRCode(version=1,
               error_correction=qr.constants.ERROR_CORRECT_H,box_size=20,border=4)
qro.add_data("https://www.youtube.com/")
qro.make(fit=True)
img = qro.make_image(fill_color="red",back_color="white")
img.save("you.png")
print("QR generated")

