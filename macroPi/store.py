import jsons as custom_json
from serializer import KeySerializer
from dataclasses import dataclass

CONFIG_FILE_NAME = "shortcuts.json"
CONFIG_TOP_LEVEL_KEYWORD = "keys"
CONFIG_REMOTE_SCAN_CODE_KEYWORD = "remote_scan_code"
CONFIG_KEY_CODE_KEYWORD = "key_code"
CONFIG_PRESSED_KEYWORD = "pressed"
CONFIG_RECORDING_KEYWORD = "recording"

def load_key_events():
    with open(CONFIG_FILE_NAME) as config_file:
        read = config_file.read()
        json_dict = custom_json.loads(read)
        config_storage = ConfigStorage(keys={})

        for json_key in json_dict[CONFIG_TOP_LEVEL_KEYWORD].values():
            
            config_events = [ConfigEvent(
                json_record[CONFIG_KEY_CODE_KEYWORD],
                json_record[CONFIG_PRESSED_KEYWORD]
            ) for json_record in json_key[CONFIG_RECORDING_KEYWORD]]
            config_key = ConfigKey(json_key[CONFIG_REMOTE_SCAN_CODE_KEYWORD], config_events)
            config_storage.keys[config_key.remote_scan_code] = config_key
    return config_storage

def store_key_events(config_storage):
    KeySerializer.create_instance()
    with open(CONFIG_FILE_NAME,'w+') as outfile:     
        outfile.write(custom_json.dumps(config_storage, {"indent": 4}))

@dataclass
class ConfigEvent:
    key_code: str
    pressed: bool

@dataclass
class ConfigKey:
    remote_scan_code: str
    recording: list[ConfigEvent]

@dataclass
class ConfigStorage:
    keys: dict[ConfigKey]