'''
python3 acorduri.py > output.html
'''

import template_composer as temp
import chords_composer as chor

filename = 'cantare.txt'
titlu = 'Poporașul Meu, Trezește-te'
ton = 'E'

temp.beginning(titlu, ton)

chor.convert2acorduri(filename)

temp.ending()