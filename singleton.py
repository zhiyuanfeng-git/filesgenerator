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

class Singleton:

    """
    Ensures that a class only has one instance.

    Usage:
    Calling the constructor when the application starts.
    Then call the get_instance method to get the the only instance
    in the subsequential code.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            raise Exception("Should call the get_instance() after this instance was created.")
        
        cls._instance = super().__new__(cls)

        return cls._instance
    
    @classmethod
    def get_instance(cls):
        return cls._instance