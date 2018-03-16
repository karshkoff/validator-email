#!/usr/bin/env python3
import re
import sys

email = sys.argv[1]
regex = "^([\w!#%$&'*+/=?^`{|}~-]+(\.[\w!#%$&'*+/=?^`{|}~-]+)*|" \
        "\"( ?[\x01-\x08\x0b\x0c\x0e-\x1f\!#-\[\]-\x7f]|\\\\[\x00-\x7f])* ?\")@" \
        "([\w!#%$&'*+/=?^`{|}~-]+(\.[\w!#%$&'*+/=?^`{|}~-]+)*|" \
        "\[( ?[\x01-\x08\x0b\x0c\x0e-\x1f\!-Z\^-~]|\\\\[\x00-\x7f])* ?\])$"

m = re.match(regex, email)
if m != None:
    print("Valid")
else:
    print("Invalid")
