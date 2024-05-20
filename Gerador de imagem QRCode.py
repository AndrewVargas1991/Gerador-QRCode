# pip install pyqrcode

import pyqrcode
import png
from pyqrcode import QRCode

endereco = input('Digite o endereço do site: ')
url = pyqrcode.create(endereco)
url.png('code.png', scale = 10)

input('QRCode criado com sucesso"\nAperte ENTER para sair...')