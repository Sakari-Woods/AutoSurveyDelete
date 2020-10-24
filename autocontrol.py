import pyautogui
import winsound
import time
import cv2
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

def noResultsFound():
	pyautogui.hotkey('alt', 'tab') #alt+tab
	pyautogui.press('left')
	pyautogui.click(389,181)
	pyautogui.click(491,255)
	pyautogui.press('down')
	pyautogui.press('right')
	pyautogui.press('right')

def resultsFound():
	pyautogui.click(1161,589)
	pyautogui.press('enter')
	pyautogui.typewrite('var target = document.querySelectorAll("tr.ng-scope");while(target.length){if(target[0].children[1].children[0].innerText == "',interval =0.1)
	pyautogui.hotkey('ctrl','v')
	pyautogui.press('backspace')
	pyautogui.typewrite('"){if(target[0].children[2].children[0].innerText==(document.querySelector("#content > div.container.ng-scope > div > div:nth-child(12) > div.panel.panel-default.i-space-t > div:nth-child(2) > div.collapsed.recipient-table.pad-t > div.form-group.ib.left-inner-addon > input").value)){if(target[0].children[4].children[0].innerText=="Incomplete"){target[0].children[5].children[1].click();target[0].children[5].children[1].click();console.log("FOUND");target[0].children[5].children[1].click();target[0].children[5].children[1].click();target[0].children[5].children[1].click();}}}target[0].remove();target = document.querySelectorAll("tr.ng-scope");}',interval=0.1)
	pyautogui.press('enter')
	pyautogui.press('enter')
	winsound.Beep(successfreq,duration)

	pyautogui.hotkey('alt', 'tab') #alt+tab
	pyautogui.press('left')
	pyautogui.click(389,181)
	pyautogui.click(491,255)
	pyautogui.press('down')
	pyautogui.press('right')
	pyautogui.press('right')


def initialize():
	pyautogui.hotkey('ctrl', 'c') #ctrl+c
	pyautogui.hotkey('alt', 'tab') #alt+tab
	pyautogui.click(295,563) #click search bar
	for x in range(5):
		pyautogui.press('pageup')

	pyautogui.click(295,563) #click search bar
	pyautogui.click(295,563) #click search bar
	pyautogui.press('right') #focus on typing box
	for x in range(10):
		pyautogui.press('backspace')
		pyautogui.press('delete')

	pyautogui.hotkey('ctrl', 'v') #ctrl+v
	pyautogui.press('enter') #enter
	pyautogui.hotkey('alt', 'tab') #ctrl+tab
	pyautogui.press('left') #move to first name
	pyautogui.hotkey('ctrl','c') #ctrl+c
	pyautogui.hotkey('alt', 'tab') #ctrl+tab
	pyautogui.hotkey('ctrl', 'f') #ctrl+f
	pyautogui.hotkey('ctrl', 'v') #ctrl+v


nofreq = 800
yesfreq = 400
successfreq = 1200
duration = 200
for i in range(1):
	initialize()
	noresults = pyautogui.locateOnScreen('0results.png', confidence=0.7)
	if(noresults == None):
		print("There are results")
		winsound.Beep(yesfreq,duration)
		resultsFound()
	else:
		print("No results found!")
		winsound.Beep(nofreq,duration)
		noResultsFound()
	print("Loop "+str(i)+" done.")
