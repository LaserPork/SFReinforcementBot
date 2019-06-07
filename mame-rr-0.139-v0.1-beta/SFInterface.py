import win32com.client
import pyautogui
from pywinauto import Application, win32defines
import pywinauto.win32functions as win32fun

app = Application().start("Notepad.exe")
#app = Application().connect(path="C:\\Windows\\System32\\notepad.exe")
w = app.top_window()

#bring window into foreground
if w.has_style(win32defines.WS_MINIMIZE): # if minimized
    win32fun.ShowWindow(w.wrapper_object(), 9) # restore window state
else:
    win32fun.SetForegroundWindow(w.wrapper_object()) #bring to front

while w.is_active():
    pyautogui.keyDown('a')
   