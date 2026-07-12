'''
python3 acorduri.py > output.html
'''

import json
import template_composer as temp
import chords_composer as chor

filename = 'example.txt'
titlu = 'Poporașul Meu, Trezește-te'
ton = 'E'

output = "../cantece/" + filename[:-3] + "html"


temp.beginning(output, titlu, ton)

chor.convert2acorduri(filename, output)

temp.ending(output)

# manually paste the printed line in the '_data.json' file
print(f'{{"title": "{titlu}", "link": "../cantece/{output}"}}')