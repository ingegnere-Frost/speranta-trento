# £x£ = align left
# $x$ = align center
# %x% = align right
# & = bold (at start and finish)
# ^ = end chords, just the rest of the lyrics

def convert2acorduri(filename='cantare.txt'):
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
        print(f'<span class="lyric" chord="{chord}">', end='')
    def print_center(chord):
        print(f'<span class="lyric" chord="{chord}" chord-align="center">', end='')
    def print_right(chord):
        print(f'<span class="lyric" chord="{chord}" chord-align="right">', end='')
    finish = '</span>'

    ended = False
    bold = False
    print(f'  {start}', end='')
    while i < len(text):
        if text[i] == '^':
            j = i
            break
        
        if text[i] == '\n':
            if bold and text[i+1] == '&':
                print(f'{finish} </b> <br>\n  ', end='')
                bold = False
                i = i+1
            else:
                print(f'{finish} <br>\n  ', end='')
            ended = True
        elif text[i] == '&':
            if not bold:
                print('<b> ', end='')
                bold = True
            else:
                print(' </b>')
                bold = False
        elif text[i] in alignment:
            if text[i] == '£':
                if not ended: print(f'{finish}\n  ', end='')
                i = i+1
                print_left(f'{text[i]}{text[i+1]}' if (i+1) in plus_chords else text[i])
            elif text[i] == '$':
                if not ended: print(f'{finish}\n  ', end='')
                i = i+1
                print_center(f'{text[i]}{text[i+1]}' if (i+1) in plus_chords else text[i])
            elif text[i] == '%':
                if not ended: print(f'{finish}\n  ', end='')
                i = i+1
                print_right(f'{text[i]}{text[i+1]}' if (i+1) in plus_chords else text[i])
            i = i+1
            ended = False
        else:
            if ended:
                print(start, end='')
                ended = False
            print(text[i], end='')
        i = i+1

    while i < len(text):
        if text[i] == '^':
            i = j+2
            print('\n  <div class="verse">\n    <br>\n    ', end='')
        
        if text[i] == '\n':
            print('<br>\n    ' if text[i-1] == '\n' else ' <br>\n    ', end='')
        elif text[i] == '&':
            if not bold:
                print('<b> ', end='')
                bold = True
            else:
                print(' </b>', end='')
                bold = False
        else:
            print(text[i], end='')
        i = i+1
    print(' <br>\n  </div>')