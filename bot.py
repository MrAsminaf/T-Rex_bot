import pyautogui
import PIL
from numpy import *
import time

class Cords:
	replayBt = [950, 550]

def ClickReplBt():
	pyautogui.click(Cords.replayBt[0], Cords.replayBt[1])

def Jump():
	pyautogui.keyDown('space')

def ImageGrab():
	box = [790, 480, 820, 520]                         
	image = PIL.ImageGrab.grab(box)
	grayImage = PIL.ImageOps.grayscale(image)
	a = array(grayImage.getcolors())
	return a.sum()

def main(): 
	while True:
		if ImageGrab () > 2000:
			Jump()

if __name__ == "__main__":
	main()