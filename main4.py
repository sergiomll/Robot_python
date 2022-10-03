from pynput import mouse, keyboard

# mouse.Button;
# mouse.Controller;

# controller=mouse.Controller();

# # Obtener la posición del mouse
# print(controller.position);

# # # Posicionamiento
# controller.position=(0,20);

# # # Moverse
# controller.move(150,32)

# # Botón derecho del ratón
# controller.click(mouse.Button.right,1)

# # Haga doble clic en el botón izquierdo
# controller.click(mouse.Button.left,2)

# # Mantenga presionado el botón izquierdo
# controller.press(mouse.Button.left)
# # Suelta el botón izquierdo
# controller.release(mouse.Button.left)

# Desplazamiento del mouse, desplazamiento del número negativo hacia abajo
# controller.scroll(0,-100);
# def on_move(x, y):
#     print(x, y)
#
#
# def on_click(x, y, button, pressed):
#     print(x, y)
#
#
# def on_scroll(x, y, dx, dy):
#     print(x, y)


# #Monitor del mouse
# with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
#     listener.join()

# Deja de escuchar o devuelve False en la devolución de llamada
# mouse.Listener.stop()


# # El siguiente es el teclado
keyboard.Key;
keyboard.Controller;
# #Control del teclado
keyboardController = keyboard.Controller();


# Mantenga el espacio
# keyboardController.press(keyboard.Key.space);
# Suelta la barra espaciadora
# keyboardController.release(keyboard.Key.space);
# Celebrar una
# keyboardController.press('a');
# keyboardController.release('a');

def on_press(key):
    pass
    # print(key)


def on_release(key):
    try:
        print(key.char)
    except AttributeError:
        print(key)
    if key == keyboard.Key.esc:
        return False


# # Supervisar las teclas del teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Deja de escuchar o devuelve False en la devolución de llamada
# keyboard.Listener.stop()
