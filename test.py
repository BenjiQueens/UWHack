#### Benji Christie ####

# UW Hackathon Test File
import qrcode
import qrcode.image.svg
import qrtools
from qrtools import QR

# qr = pyqrcode.create("something this that")
# qr.png("horn.png", scale = 6)

qr = qrtools.QR()
qr.decode("QR.jpg")
print(qr.data)

print("test")

#

if method == 'basic':
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    factory = qrcode.image.svg.SvgFragmentImage
else:
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make('data', image_factory=factory)
