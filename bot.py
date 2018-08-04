import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *

def Jump():
	pyautogui.keyDown('space')

def ImageSum():
    box = [770, 380, 850, 450]
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
	while True:
		if ImageSum () > 6000:
			Jump()

if __name__ == "__main__":
	main()
