from pynput import *

coordinates = [];

def on_click(x, y, button, pressed):
    # append coords twice for topleft and rightbottom
    if(pressed):
        coordinates.append([x, y])
        print(f"Get {len(coordinates)} coordinate.")
    if(len(coordinates) >= 2):
        return False


def get_coords():
    with mouse.Listener(on_click = on_click) as listen:
        listen.join()
    return coordinates

__all__ = ['get_coords']
