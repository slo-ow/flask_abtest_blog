import pyqrcode
import png

qrcode = pyqrcode.create('https://9c10-211-0-208-154.ngrok-free.app/main')
qrcode.svg('qrcode_blog.svg', scale=8)
qrcode.eps('qrcode_blog.eps', scale=2)