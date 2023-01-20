from aqt import mw
from aqt.utils import *
from aqt.browser import *

def show_dialog():
    qid_list, ok = aqt.utils.getText(prompt="Paste UWorld question IDs:")

    if ok:
        valid_input = check_integrity(qid_list)

        if valid_input:
            final_list = [int(x.strip()) for x in qid_list.split(",")]
            search(final_list)
        else:
            aqt.utils.show_warning("Invalid input")

def check_integrity(ids):
    processed = ids.split(",")

    for qid in processed:
        if not qid.strip().isdigit():
            return False

    return True

def search(ids):
    query = create_query(ids)
    b = aqt.browser.browser.Browser(mw=mw)
    b.search_for(search=query)

def create_query(ids):
    query = ""

    for tag in ids:
        if tag == ids[0]:
            query = "tag:*UWorld*::" + str(tag)
        else:
            query += " OR tag:*UWorld*::" + str(tag)

    return query

action = QAction("Find cards from UWorld test", mw)
qconnect(action.triggered, show_dialog)
mw.form.menuTools.addAction(action)
