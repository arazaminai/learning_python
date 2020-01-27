#!/usr/bin/python
# mclip - A multi-clipboard program.

import sys
from pyperclip import copy




text = {"agree": """Yes, I agree, that sounds fine to me.""",
        "busy": """Sorry, can we do this later this week or next week?""",
        "upsell": """Would you consider making this a monthly donation?"""}




def help_(text):
    print("Usage: mclip.py [keyphrase] \nkeyphrases:")
    for k, v in text.items():
        k = k.ljust(20)
        print("\t%s%s" % (k, v))




if len(sys.argv) < 2:
    help_(text)
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    copy(text[keyphrase])
    print("Text for %s copied to clipboard." % (keyphrase))
    sys.exit
elif keyphrase == "-h" or keyphrase =="--help":
    help_(text)
    sys.exit()
else:
    print("%s not found" % (keyphrase))
    help_(text)
    sys.exit()
