import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=18,border=18,)
qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&t=1152s&ab_channel=WsCubeTech")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("wscube_web.png")