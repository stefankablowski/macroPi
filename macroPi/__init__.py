from keys import record, replay
from store import store_key_events, load_key_events, __init__

arr = record()
print(arr)
store_key_events(arr)
for elem in arr:
    print(elem[0])