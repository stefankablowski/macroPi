from dataclasses import dataclass

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