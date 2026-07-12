'''
python3 acorduri.py > output.html
'''

import template_composer as temp
import chords_composer as chor

filename = 'test.txt'
titlu = 'Izvorul, izvorul, Izvor de bucurii - De când urmez pe Isus'
ton = 'G'

output = "../cantece/" + filename[:-3] + "html"


temp.beginning(output, titlu, ton)

chor.convert2acorduri(filename, output)

temp.ending(output)

# manually paste the printed line in the '_data.json' file
print(f'{{"title": "{titlu}", "link": "{output}"}}')