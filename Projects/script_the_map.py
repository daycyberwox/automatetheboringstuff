import webbrowser, sys #import the web browser and sys module

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) >1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste


# htttps://www.google.com/place/<ADDDRES>
webbrowser.oppen('htttps://www.google.com/place' + address)