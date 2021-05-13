import re
emoji = input("Enter an Emoji like (lol, rofl, lmk, smh):")
if re.match(emoji, 'lol', re.IGNORECASE):
    print("Laugh Out Loud !!!")
elif re.match(emoji, 'rofl', re.IGNORECASE):
    print("Roll on the Floor Laughing :D")
elif re.match(emoji, 'lmk', re.IGNORECASE):
    print("Let Me Know :P")
elif re.match(emoji, 'smh', re.IGNORECASE):
    print("Shaking My Head :X")
else:
    print("Not a Known Emoji :(")