# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live
from USB_X_Session import USB_X_Session

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return USB_X_Session(c_instance)


# local variables:
# tab-width: 4
