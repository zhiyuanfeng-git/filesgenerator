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

from utility import open_file_r
from constants import UTF8,IGNORE_FILE
class Ignore:
    """Ignores some files that configured in the ignore.txt"""

    ignores = set()

    @staticmethod
    def load():
        try:
            file = open_file_r(IGNORE_FILE, encoding=UTF8)
            for line in file:
                Ignore.ignores.add(line.strip())
        except Exception as e:
            print(e)
        finally:
            file.close()

    def is_ignore(file_name) -> bool:
        if file_name in Ignore.ignores:
            return True
        return False