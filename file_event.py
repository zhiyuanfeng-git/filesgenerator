# Copyright 2024 Feng ZhiYuan <feng.zhiyuan@outlook.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pargen.event import Event,EventType
from enum import Enum

class EventSubType(Enum):
    UNDEFINED = 0
    SINGLE = 1
    MULTIPLE = 2

class FileEventType(EventType):
    NONE = 0
    PARSER = 1
    
class ParserEvent(Event):
    
    def __init__(self):
        super().__init__(FileEventType.PARSER)
        self.data = None
        self.file_name = None
        self.subType = EventSubType.UNDEFINED
    
    def cleanup(self):
        self.data = None
        self.file_name = None
        self.subType = EventSubType.UNDEFINED
        return super().cleanup()