# Repository for 'speranta-trento.org' website

Even though the content of the website is primarly in Romanian, some things, such as this readme file, or the "Version History" tab, are written in English, so the project can be open to anyone.

The main objective of this website is to provide the lyrics of as many Romanian Christian songs as possible, together with the chords (for instruments) and the ability to change them (still WIP), and in the future, easy import option for software like FreeShow, and maybe even a download option for the '.json' file (together with other stuff regarding FreeShow, like templates), and/or '.odp' files for direct use with LibreOffice Impress or MS Office PowerPoint.


## Links to the various sources

[![Website Homepage](https://img.shields.io/badge/Website-Homepage-lightblue?style=for-the-badge)](https://speranta-trento.org/) &nbsp;
[![Static Badge](https://img.shields.io/badge/Resurse-Cre%C8%99tine-salmon?style=for-the-badge)](https://www.resursecrestine.ro/) &nbsp;
[![Github Repo](https://img.shields.io/badge/github-repo-blue?logo=github)](https://github.com/ingegnere-Frost/speranta-trento) &nbsp;
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Why this website?

It all started when a fellow brother in Christ asked me to make a PDF file with all the songs that they sing in the church, together with the chords above the lyrics. But, sometimes, the chords (available online) were in the wrong tone, so a simple screenshot or copy-and-paste wasn't enough, and the chords needed to be modified. And that's when I though about this idea. Hosting a simple website like this costs nothing, the domain is very cheap, and it's a nice project with a great future vision.

Seeing also how I wanted to switch from the classic "BibleShow + PowerPoint" system that most churches use, to FreeShow, I also started to expand my horizon: eventually I want to add on this website the compatibility with the quick-text-import of the app (where you just copy and paste the song, and you have it ready), maybe even adding the download of the show files for the app, already formatted and stuff, share templates, the bibles (which can already be found online, but they don't seem to have the books' names in the '.xml' files; also, an idea was to add Jesus' words in red on the bible, that can be seen also when displayed on FreeShow, but one step at a time), and maybe even more.

Almost all the stuff comes from <u>Resurse Creștine</u>. I'm not trying to create an alternative to that, because it is a very good website, that's way more user friendly, with a lot of functionality, and EVEN MORE material, which I could never. My website is more oriented to the artists/singers, and eventually for developers, and generally for the IT people in the churches. And besides, most of these songs are old, available everywhere, but more easily on that site.

This is a static website, so there isn't much code at all. The heavy part comes from importing all the songs: I have to manually search for them (making sure that they have the accents and everything), correct the syntax, seach for a version with the chords (acorduri), add them, and then I'm done. 

I know that for some experts looking at the code, it might not seem very good, but I've tried my best; I'm not very proficient with **HTML**, and not proficient at all with **JavaScript**. I say this with a heavy heart, and I'm not really happy about it, but a good part of the code was generated with LLMs. Now, the idea and the execution was all from me, but since I don't know how to use the two aformentioned coding languages, that was my "best" course of action. But, the **Python** converter that I built, is all 100% me (*it ain't much, but it's honest work!*). Originally, it took me like half an hour for a single song, but then I said *"Why do I have to manually write every single line of code? Let me try with a Python script..."* and then, in like half a day, I made a script that does all the main stuff.
The script corrects the accents on "Ș/ș" and "Ț/ț" characters, which can contain the wrong type of accent (with Cedilla, that looks very similar). Then, it adds the chords, and the bold sections, according to the input text file.


### Python Converter

Simple Python script with two modules. In 'acorduri.py' just add the title, tone, name of the '.txt' file with the song in "raw" format, then run
```bash
python3 acorduri.py
```
Now with version 2.0.1, it will automatically add the song to the correct folder, and it will print in the terminal the line that needs to be appended to the '_data.json' file. 
More details are written in the main Python file, or just look at the available file for an example.
Manual corrections may be required, so keep an eye out!