import threading
import pickle
from enum import Enum
from pynput.keyboard import Key, Listener, Controller

class key_state(Enum):
    pressed = True
    released = False

keyboard = Controller()
recorded_key_events = []
most_recent_event = None
lock = threading.Lock()

def event_equals(ev_1, ev_2):
    # deep equal comparison of object attributes
    return pickle.dumps(ev_1) == pickle.dumps(ev_2)

def create_key_event(key, pressed):
    return (key, pressed)

def record_unique_key_event(current_key_event):
    global most_recent_event
    with lock:
        if(event_equals(most_recent_event,current_key_event)):
            pass
        else:
            recorded_key_events.append(current_key_event)
            most_recent_event = current_key_event
            print(current_key_event)

def on_press(key):
    current_key_event = create_key_event(key, key_state.pressed)
    record_unique_key_event(current_key_event)

def on_release(key):
    current_key_event = create_key_event(key, key_state.released)
    record_unique_key_event(current_key_event)
    if key == Key.esc:
        # Stop listener
        print("quitting script")
        return False

def execute_key_event(key_event):
    ev_key = key_event[0]
    ev_state = key_event[1]
    
    if(ev_state == key_state.pressed):
        keyboard.press(ev_key)
    elif(ev_state == key_state.released):
        keyboard.release(ev_key)
    else:
        raise TypeError("invalid key event")

# blocking
def record():
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
    return recorded_key_events

def replay(event_list):
    for key_event in event_list:
        execute_key_event(key_event)
