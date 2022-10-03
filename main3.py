import pyautogui

# size = pyautogui.size()
# print(size)
# pos = pyautogui.position()
# print(pos)

# x = 100
# y = 100
# num_seconds = 2
# pyautogui.moveTo(x, y, duration=num_seconds)
# pyautogui.moveRel(100, 100, duration=num_seconds)

# x = 700
# y = 500
# num_of_clicks = 3
# secs_between_clicks = 1
# pyautogui.click(x=x, y=y, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

# pyautogui.scroll(-1000)
# pyautogui.scroll(500)
# pyautogui.mouseDown(x=x, y=y, button='left')
# pyautogui.mouseUp(x=x, y=y, button='left')

# secs_between_keys = 0.5
# pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)
# keys = pyautogui.KEYBOARD_KEYS

# pyautogui.hotkey('ctrl', 'c')

# pyautogui.keyDown('c')
# pyautogui.keyUp('c')

# pyautogui.alert('This displays some text with an OK button.')
# press = pyautogui.confirm('This displays text and has an OK and Cancel button.')
# print(press)
# user = pyautogui.prompt("Ingrese su nombre de usuario", "Iniciar sesión")
# print(user)
# pas = pyautogui.password(text='', title='', default='', mask='*')
# print(pas)

# im = pyautogui.screenshot()  # returns a Pillow/PIL Image object
# im = pyautogui.screenshot(region=(0,0, 300, 400))
# im.getpixel((100, 200))
# px = pyautogui.pixel(100, 200)
# print(px)
# pyautogui.pixelMatchesColor(100, 200, (130, 135, 144), tolerance=10)
# pyautogui.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file
# pyautogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found
# pyautogui.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y
# button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9)

# im = pyautogui.screenshot("test.png", region=(478,30, 26,24))
# loc = pyautogui.locateOnScreen("test.png", region=(450,0, 100, 100))
loc = pyautogui.locateCenterOnScreen("test.png", region=(450,0, 100, 100))
# loc = pyautogui.locateOnScreen("test.png", region=(450,0, 100, 100), confidence=0.9)
# You need to have OpenCV installed for the confidence keyword to work.
print(loc)



























