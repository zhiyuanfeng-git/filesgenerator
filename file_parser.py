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

from pargen.parsers import Parser
from pargen.status import Status
from singleton import Singleton
from file_event import EventSubType
from utility import is_empty_file,open_file_r,extract_file_name
from constants import UTF8

class FileParser(Parser, Singleton):
    """
    As a subclass of The Parser.
    Accountable to parse specific files, and pass some data to FileGenerator
    via ParserEvent for generating some specific format files.
    """

    def __init__(self, event, generator):
        Parser.__init__(self, event, generator)

    def parse(self, *args) -> Status | None:
        file_path = args[0]
        file_name = extract_file_name(file_path)
        try:
            file = open_file_r(file_path, UTF8)
            if is_empty_file(file):
                print(f"Can't parse the empty file {file_path}")
                return Status.ERROR_INTERRUPTED
            
            self.__parse_file(file, file_name)
        except Exception as e:
            print(f"Open Error,file:{file_path},e:{e}")
        finally:
            file.close()

    @staticmethod
    def parse_number(str_line):
        first_ch = str_line[0]
        if first_ch.isdigit():
            num_str = ''
            for ch in str_line:
                if ch.isdigit():
                    num_str += ch
                else:
                    break
            return int(num_str)
        else:
            return str_line

    def __parse_single(self, file):
        self._event.subType = EventSubType.SINGLE
        result_str = ''
        for line in file:
            str_line = line.strip()
            if result_str == '':
                result_str += str_line
            else:
                result_str += f'\n# {str_line}'

        self._event.data = result_str

    def __parse_multiple(self, file):
        self._event.subType = EventSubType.MULTIPLE
        self._event.data = []
        group_line = 0
        group_str = ''
        last_ret = None
        for line in file:
            str_line = line.strip()
            if str_line != '':
                last_ret = FileParser.parse_number(str_line)
                if type(last_ret) == int:
                    if group_line > 0:
                        self._event.data.append(group_str)
                        group_str = ""

                    group_line += 1
                    group_str += str_line
                elif type(last_ret) == str:
                    group_str += f"\n# {str_line}"

        if group_line > 0 and group_line > len(self._event.data):
            self._event.data.append(group_str)
    
    def __parse_file(self, file, file_name):
        first_str = file.read(1)
        file.seek(0)
        self._event.file_name = file_name
        if not first_str.isdigit():
            self.__parse_single(file)
        else:
            self.__parse_multiple(file)

            