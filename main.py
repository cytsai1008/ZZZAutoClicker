import random
import time

import psutil
import vgamepad as vg
import win32gui
import win32process

import screen_ocr

gamepad = vg.VX360Gamepad()
time.sleep(1)


def active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(
            win32gui.GetForegroundWindow())  # This produces a list of PIDs the active window relates to
        return psutil.Process(pid[-1]).name()  # pid[-1] is the most likely to survive to last longer
    except psutil.NoSuchProcess:  # Catch the error caused by the process no longer existing
        # retry
        return active_window_process_name()


def keep_active():
    while True:
        proc_name = active_window_process_name()
        if proc_name.lower() == "zenlesszonezero.exe":
            break
        else:
            print(f"Current window is {proc_name}")
        time.sleep(.5)


def press_button(button, wait_time=0.1):
    gamepad.press_button(button=button)
    gamepad.update()
    time.sleep(wait_time)
    gamepad.release_button(button=button)
    gamepad.update()


while True:
    proc_name = active_window_process_name()
    if proc_name.lower() == "zenlesszonezero.exe":
        break
    else:
        print(f"Current window is {proc_name}")
    time.sleep(1)

while True:
    randsec = (random.randint(0, 5)) / 10
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, 0.5 + randsec)
    print("A released")

    keep_active()

    screen_text = screen_ocr.screen_ocr()

    if "市政維護" not in screen_text and "HoYoLAB" not in screen_text and "進入遊戲" not in screen_text:
        print("Got it")
        break

    randsec = (random.randint(0, 5)) / 10
    time.sleep(7.4 + randsec)

    randsec = (random.randint(0, 5)) / 10
    press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B, 0.5 + randsec)
    print("B released")

    keep_active()
