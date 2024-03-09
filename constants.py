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

"""
Stores the global constant variable
"""

IGNORE_FILE = "ignore.txt"
SOURCE_DIR = "files"
GENERATE_DIR = "gens"
UTF8 = "utf-8"

PY_SUFFIX = ".py"
IMPORT_SYS = "import sys"
MAIN_FUNCTION = "def main():\n   return 0\n"
PY_ENTRY = "if __name__ == '__main__':\n  sys.exit(main())"