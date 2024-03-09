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

import os

def scan_dir(path):
    return os.scandir(path)

def open_file_r(file_name, encoding: str | None = None):
    file = open(file_name, 'r' , encoding=encoding)
    return file

def open_file_w(file_name, encoding: str | None = None):
    file = open(file_name, 'w', encoding=encoding)
    return file

def create_dir(directory_path,  exist_ok=True):
    directory = os.path.dirname(directory_path)
    if directory:
        os.makedirs(directory, exist_ok=exist_ok)

def is_empty_file(file):
    file.seek(0, os.SEEK_END)
    if file.tell() == 0:
        return True
    file.seek(0, os.SEEK_SET)
    return False
