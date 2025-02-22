import pytest
from pynput.mouse import Controller, Button
from unittest.mock import patch

mouse = Controller()

#----------------------------------------Get Mouse Position----------------------------------------#
def get_mouse_position():
    """
    Returns the Coordinates of current mouse position.
     
    """
    return dict(zip(("x","y"),mouse.position))


def test_get_mouse_position():
    # Check Returns Structure 
    assert get_mouse_position().__class__.__name__ == "dict"
    assert len(get_mouse_position()) == 2
    
    # Check Values Structure
    for val in get_mouse_position().values():
        assert val.__class__.__name__ == "int"

#----------------------------------------Move Mouse----------------------------------------#
# Original Function
def move_mouse(position):
    """
    Moves the mouse to a position 
    
    Parameters:
    position(tuple[int,int]): x and y coordinates of the new position. 
    """
    mouse.position = position
    
@pytest.mark.parametrize("position", [(100,10),
                                      (254,500)])
def test_move_mouse(position):
    move_mouse(position)
    # Check if mouse position has changed
    assert position == tuple(get_mouse_position().values())
    
#----------------------------------------Click Mouse----------------------------------------#
# Original Function
def click_mouse(button,count=1):
    """
    Clicks the button * times.
    
    Parameters:
    - type(string): left or right or other buttons in the mouse.
    - count(int): number of clicks.
    """
    
    if button == "left":
        mouse.click(Button.left, count)
    
    if button == "right":
        mouse.click(Button.right, count)

@pytest.mark.parametrize("button, count", [
    ("left", 1),
    ("right", 2),
])
def test_click_mouse(button, count):
    click_mouse(button, count)
    # Manual Testing
    
    