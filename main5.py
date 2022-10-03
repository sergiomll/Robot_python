from pynput import keyboard
import pyautogui
import time

# #Control del teclado
keyboardController = keyboard.Controller()


def get_info():
    currentMouseX, currentMouseY = pyautogui.position()
    px = pyautogui.pixel(currentMouseX, currentMouseY)
    print(f"({currentMouseX},{currentMouseY}) -> {px}")


def on_press(key):
    pass
    # print(key)


def on_release(key):
    try:
        # print(key.char)
        if key.char == 'i':
            get_info()
    except AttributeError:
        print(key)
    if key == keyboard.Key.esc:
        return False  # detener escucha teclado


# # The event listener will be running in this block
# with keyboard.Events() as events:
#     for event in events:
#         if event.key == keyboard.Key.esc:
#             break
#         else:
#             print('Received event {}'.format(event))

# Supervisar las teclas del teclado bloqueando la ejecucion
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Deja de escuchar o devuelve False en la devolución de llamada
# keyboard.Listener.stop()


# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()
