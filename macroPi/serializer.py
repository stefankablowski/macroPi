from pynput.keyboard import Key, KeyCode
import jsons as custom_json

class KeySerializer:

    instance = None

    @classmethod
    def create_instance(self):
        if(KeySerializer.instance == None):
            ks = KeySerializer()
            KeySerializer.instance = ks
            custom_json.set_serializer(ks.serialize_key, Key)
            custom_json.set_serializer(ks.serialize_key_code, KeyCode)

    def serialize_key(self, obj: Key, **kwargs):
        return str(obj)

    def serialize_key_code(self, obj: KeyCode, **kwargs):
        return str(obj)