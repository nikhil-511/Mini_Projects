import pywhatkit
import pyautogui
import webbrowser as wb
"""
for i in range(5):
    pywhatkit.sendwhatmsg('+9192989 09998',
                          'This message is sent using python program',17,36)
    pyautogui.press("enter")
    for i in range(5):
    pyautogui.press("hi")
    pyautogui.press("enter")
"""

chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
wb.get(chrome_path).open('web.whatsapp.com')

