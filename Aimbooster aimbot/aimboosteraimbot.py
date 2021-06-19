import pyautogui,keyboard,time

#This program is an aimbot for aimbooster.com
#NOTE: PLEASE USE F11 WHEN PLAYING TO AVOID THE MOUSE FLICKING TO THE TAB ICON

print("Press s to start/stop the program")

#Main function for when the user has started the program
def started():
    #Starts the loop while s isnt pressed
    while keyboard.is_pressed('s') == False:
        try:
            #looking for target (using image of target.png)
            x,y = pyautogui.locateCenterOnScreen("target.png",confidence = 0.8,grayscale=True,region=(482,65,984,780))
            #Clicks on target
            pyautogui.click(x,y)
        except:
            pass
    print("Aimbot Stopped")

#Loop waiting for start keypress
while True:
    keyboard.wait("s")
    time.sleep(.3)
    print("Aimbot Started")
    started()

        
