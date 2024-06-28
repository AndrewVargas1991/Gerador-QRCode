# pip install pyqrcode
# pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode

endereco = input('Digite algo: ')
url = pyqrcode.create(endereco)
url.png('code.png', scale = 10)

input('QRCode criado com sucesso"\nAperte ENTER para sair...')
