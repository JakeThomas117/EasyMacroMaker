import keyboard
import mouse
import time

def play(events):
    print("PLAYING")
    last_time = None
    for e in events:
        if last_time is not None:
            time.sleep((e.time - last_time) / 2.5)
            if keyboard.is_pressed('esc'):
                print("\n$$$MANUAL OVERRIDE: EXECUTION STOPPED$$$\n")
                break
        last_time = e.time
        
        if isinstance(e, mouse.ButtonEvent) or isinstance(e, mouse.WheelEvent) or isinstance(e, mouse.MoveEvent):
            mouse.play([e], speed_factor=0)
        else:
            keyboard.play([e], speed_factor=0)
    print("DONE\nPress F8 to play or shift+esc to exit.\nPress esc during execution to exit immediately.")
            
print("============================\nPress esc to start recording.")
keyboard.record(until='esc')
print("\nRECORDING\nPress esc to stop recording.")

recorded = []
mouse.hook(recorded.append)
keyboard.hook(recorded.append)
keyboard.wait('esc')
mouse.unhook(recorded.append)
keyboard.unhook(recorded.append)
print("\nRecording stopped\nPress F8 to play or shift+esc to exit.\nPress esc during execution to exit immediately.")
   
keyboard.add_hotkey('F8', lambda: play(recorded))

keyboard.wait('shift+esc')