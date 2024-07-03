import random
import time

import psutil
import vgamepad as vg
import win32gui
import win32process

gamepad = vg.VX360Gamepad()
time.sleep(1)


def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(
        win32gui.GetForegroundWindow())  # This produces a list of PIDs the active window relates to
    return psutil.Process(pid[-1]).name()  # pid[-1] is the most likely to survive to last longer


while True:
    proc_name = active_window_process_name()
    if proc_name.lower() == "zenlesszonezero.exe":
        break
    else:
        print(f"Current window is {proc_name}")
    time.sleep(1)

while True:
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button
    gamepad.update()  # send the updated state to the computer
    print("A pressed")

    randsec = (random.randint(0, 5)) / 10
    time.sleep(.5 + randsec)

    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button
    gamepad.update()  # send the updated state to the computer
    print("A released")

    randsec = (random.randint(0, 5)) / 10
    time.sleep(7.4 + randsec)

    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    print("B pressed")

    randsec = (random.randint(0, 5)) / 10
    time.sleep(.5 + randsec)

    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    print("B released")
