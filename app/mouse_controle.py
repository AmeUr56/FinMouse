from pynput.mouse import Controller, Button

mouse = Controller()

def get_mouse_position():
    """
    Returns the Coordinates of current mouse position.
     
    """
    return dict(zip(("x","y"),mouse.position))

        
def move_mouse(position):
    """
    Moves the mouse to a position 
    
    Parameters:
    position(tuple[int,int]): x and y coordinates of the new position. 
    """
    mouse.position = position


def click_mouse(button,count=1):
    """
    Clicks the button # times.
    
    Parameters:
    - type(string): left or right or other buttons in the mouse.
    - count(int): number of clicks.
    """
    
    if button == "left":
        mouse.click(Button.left, count)
    
    if button == "right":
        mouse.click(Button.right, count)