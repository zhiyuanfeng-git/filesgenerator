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

from pargen.generators import Generator
from singleton import Singleton
from file_event import EventSubType
from file_write_mixin import FileWriteMixin
from constants import GENERATE_DIR,PY_SUFFIX

class FileGenerator(Generator, Singleton, FileWriteMixin):
    """
    As a subclass of Generator.
    Accountable for generating some specific format files by the parameters
    with ParserEvent.
    Meanwhile, generate the file with the template data in the FileWriteMixin.
    """

    def generate(self, event):
        data = event.data
        file_name = event.file_name
        match(event.subType.value):
            case EventSubType.SINGLE.value:
                FileGenerator.__handle_single(file_name, data)
            case EventSubType.MULTIPLE.value:
                FileGenerator.__handle_multiple(file_name, event.data)
            case _:
                raise Exception("Undefined EventSubType")
    
    @staticmethod
    def __build_file_path(file_name, suffix = None):
        if suffix:
            return f"{GENERATE_DIR}/{file_name}/{file_name}_{suffix}{PY_SUFFIX}"
        return f"{GENERATE_DIR}/{file_name}/{file_name}{PY_SUFFIX}"

    @staticmethod
    def __handle_single(file_name, data):
        file_path = FileGenerator.__build_file_path(file_name)
        FileGenerator.__generate_file(file_path, data)

    @staticmethod
    def __iterate_multiple_lines(data):
        for item in data:
            yield item

    @staticmethod
    def __handle_multiple(file_name, data):
        gen = FileGenerator.__iterate_multiple_lines(data)
        for index, line_data in enumerate(gen, start=1):
            file_path = FileGenerator.__build_file_path(file_name,index)
            FileGenerator.__generate_file(file_path, line_data)

    @staticmethod
    def __generate_file(file_path, content):
        FileWriteMixin.write_file_with_template(file_path, content)
        print(f"Generated the file {file_path}")

