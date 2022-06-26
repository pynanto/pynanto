import json


class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def serialize(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def deserialize(j):
    return json.loads(j,)

from dataclasses import dataclass
from typing import Dict, List


class DisplayMode(str):
    Band = "band"
    Line = "line"
    Label = "label"
    Hidden = "hidden"


@dataclass(init=False)
class Column:
    name: str
    display_mode: DisplayMode
    values_color: Dict[str, str] = None
    color: str = None
    labels: List[str] = None
