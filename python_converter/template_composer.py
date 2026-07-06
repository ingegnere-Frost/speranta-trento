tonalitate = {'C':0,
              'C#':1,
              'D':2,
              'D#':3,
              'E':4,
              'F':5,
              'F#':6,
              'G':7,
              'G#':8,
              'A':9,
              'A#':10,
              'B':11}
octave = [
  ['''      <option value="0" selected>Do</option>
      <option value="1">Do#</option>
      <option value="2">Re</option>
      <option value="3">Re#</option>
      <option value="4">Mi</option>
      <option value="5">Fa</option>
      <option value="6">Fa#</option>
      <option value="7">Sol</option>
      <option value="8">Sol#</option>
      <option value="9">La</option>
      <option value="10">La#</option>
      <option value="11">Si</option>'''],
  [],
  ['''      <option value="-2">Do</option>
      <option value="-1">Do#</option>
      <option value="0" selected>Re</option>
      <option value="1">Re#</option>
      <option value="2">Mi</option>
      <option value="3">Fa</option>
      <option value="4">Fa#</option>
      <option value="5">Sol</option>
      <option value="6">Sol#</option>
      <option value="7">La</option>
      <option value="8">La#</option>
      <option value="9">Si</option>'''],
  [],
  ['''      <option value="-4">Do</option>
      <option value="-3">Do#</option>
      <option value="-2">Re</option>
      <option value="-1">Re#</option>
      <option value="0" selected>Mi</option>
      <option value="1">Fa</option>
      <option value="2">Fa#</option>
      <option value="3">Sol</option>
      <option value="4">Sol#</option>
      <option value="5">La</option>
      <option value="6">La#</option>
      <option value="7">Si</option>'''],
  ['''      <option value="-5">Do</option>
      <option value="-4">Do#</option>
      <option value="-3">Re</option>
      <option value="-2">Re#</option>
      <option value="-1">Mi</option>
      <option value="0" selected>Fa</option>
      <option value="1">Fa#</option>
      <option value="2">Sol</option>
      <option value="3">Sol#</option>
      <option value="4">La</option>
      <option value="5">La#</option>
      <option value="6">Si</option>'''],
  [],
  ['''      <option value="-7">Do</option>
      <option value="-6">Do#</option>
      <option value="-5">Re</option>
      <option value="-4">Re#</option>
      <option value="-3">Mi</option>
      <option value="-2">Fa</option>
      <option value="-1">Fa#</option>
      <option value="0" selected>Sol</option>
      <option value="1">Sol#</option>
      <option value="2">La</option>
      <option value="3">La#</option>
      <option value="4">Si</option>'''],
  [],
  ['''      <option value="-9">Do</option>
      <option value="-8">Do#</option>
      <option value="-7">Re</option>
      <option value="-6">Re#</option>
      <option value="-5">Mi</option>
      <option value="-4">Fa</option>
      <option value="-3">Fa#</option>
      <option value="-2">Sol</option>
      <option value="-1">Sol#</option>
      <option value="0" selected>La</option>
      <option value="1">La#</option>
      <option value="2">Si</option>'''],
  [],
  ['''      <option value="-11">Do</option>
      <option value="-10">Do#</option>
      <option value="-9">Re</option>
      <option value="-8">Re#</option>
      <option value="-7">Mi</option>
      <option value="-6">Fa</option>
      <option value="-5">Fa#</option>
      <option value="-4">Sol</option>
      <option value="-3">Sol#</option>
      <option value="-2">La</option>
      <option value="-1">La#</option>
      <option value="0" selected>Si</option>''']
]

def beginning(title, tone):
  print(f'''<!DOCTYPE html>
<html lang="ro">
<head>
  <title>{title}</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../styles.css">
  <link rel="icon" type="image/png" href="/favicons/favicon-96x96.png" sizes="96x96" />
  <link rel="icon" type="image/svg+xml" href="/favicons/favicon.svg" />
  <link rel="shortcut icon" href="/favicons/favicon.ico" />
  <link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon.png" />
  <link rel="manifest" href="/favicons/site.webmanifest" />
</head>
<body>
  <div class="noScreen" style="color:red;"><h3>{title}</h3></div>
  
  <div class="noPrint">
    <label for="showChords">Acorduri</label>
    <input type="checkbox" id="showChords" checked>  
    <br>
    <label for="transposeSelect">Tonalitate: </label>
    <select id="transposeSelect">''')
  
  print(octave[tonalitate[tone]][0])
  
  print(f'''    </select>
    <br>
    <br>
  </div>\n''')

def ending():
  print(f'''  <script src="../scripts.js"></script>
  <script> setupChordZoom(100, 100); </script>
  
  <div class="noPrint">
    <br>
    <br>
    <a href="../index.html">Home</a>
  </div>
</body>
</html>''', end='')