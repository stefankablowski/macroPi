import jsons as custom_json
import json
from serializer import KeySerializer
from pynput.keyboard import Key, Listener, KeyCode

def store_key_events(arr):
    KeySerializer.create_instance()
    with open('shortcuts.txt','w+') as outfile:
        for key_event in arr:
            jsonstr = custom_json.dump(key_event[0]) + '\n'
            outfile.write(jsonstr)
            #print(jsonstr)

def load_key_events():
    pass
