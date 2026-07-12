# £x£ = align left
# $x$ = align center
# %x% = align right
# & = bold (at start and finish)
# ^ = end chords, just the rest of the lyrics

def convert2acorduri(filename, output):
    wrong =   ['Ş','ş','Ţ','ţ']
    correct = ['Ș','ș','Ț','ț']

    with open(filename, 'r') as file:
        text = file.read()

    for i in range(0, len(wrong)):
        text = text.replace(wrong[i], correct[i])

    alignment = ['£','$','%']
    plus_chords = ['#','b','7']

    start = '<span class="lyric">'
    def print_left(chord):
        html.write(f'<span class="lyric" chord="{chord}">')
    def print_center(chord):
        html.write(f'<span class="lyric" chord="{chord}" chord-align="center">')
    def print_right(chord):
        html.write(f'<span class="lyric" chord="{chord}" chord-align="right">')
    finish = '</span>'

    ended = False
    bold = False
    with open(output, 'a') as html:
        i = 0
        if text[i] == '&':
            html.write(f'  <b> {start}')
            bold = True
            i = i+1
        while i < len(text):
            if text[i] == '^':
                j = i
                break
            
            if text[i] == '\n':
                if bold and text[i+1] == '&':
                    html.write(f'{finish} </b> <br>\n  ')
                    bold = False
                    i = i+1
                else:
                    html.write(f'{finish} <br>\n  ')
                ended = True
            elif text[i] == '&':
                if not bold:
                    html.write('<b> ')
                    bold = True
                else:
                    html.write(' </b>')
                    bold = False
            elif text[i] in alignment:
                if text[i] == '£':
                    if not ended: html.write(f'{finish}\n  ')
                    i = i+1
                    print_left(f'{text[i]}{text[i+1]}' if (i+1) in plus_chords else text[i])
                elif text[i] == '$':
                    if not ended: html.write(f'{finish}\n  ')
                    i = i+1
                    print_center(f'{text[i]}{text[i+1]}' if (i+1) in plus_chords else text[i])
                elif text[i] == '%':
                    if not ended: html.write(f'{finish}\n  ')
                    i = i+1
                    print_right(f'{text[i]}{text[i+1]}' if (i+1) in plus_chords else text[i])
                i = i+1
                ended = False
            else:
                if ended:
                    html.write(start)
                    ended = False
                html.write(text[i])
            i = i+1

        while i < len(text):
            if text[i] == '^':
                i = j+2
                html.write('\n  <div class="verse">\n    <br>\n    ')
            
            if text[i] == '\n':
                html.write('<br>\n    ' if text[i-1] == '\n' else ' <br>\n    ')
            elif text[i] == '&':
                if not bold:
                    html.write('<b> ')
                    bold = True
                else:
                    html.write(' </b>')
                    bold = False
            else:
                html.write(text[i])
            i = i+1
        html.write(' <br>\n  </div>\n')