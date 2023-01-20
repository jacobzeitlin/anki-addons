import webbrowser

from aqt import mw
from aqt.utils import *

def open_link():
    webbrowser.open("https://www.medschoolGPT.com")

action = QAction("medschoolGPT", mw)
qconnect(action.triggered, open_link)
mw.form.menuTools.addAction(action)
