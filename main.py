#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
Author: Feng ZhiYuan <feng.zhiyuan@outlook.com>
Github: https://github.com/zhiyuanfeng-git/filesgenerator

Description:
This is a file parser and generator tool.
"""

# FileParser单例
# Observable dictionary
# file head comments
# submodule in github
# upload to github
import sys
from utility import scan_dir
from ignore import Ignore
from file_parser import FileParser
from file_generator import FileGenerator
from file_event import ParserEvent
from constants import SOURCE_DIR

def __parse_file(file_path):
    FileParser.get_instance()(file_path)

def __do_generate():
    files_to_process = scan_dir(SOURCE_DIR)
    for file_to_process in files_to_process:
        file_path = file_to_process.path
        file_name = file_to_process.name
        if Ignore.is_ignore(file_name):
            print(f'Ignore file: {file_name}')
            continue
        __parse_file(file_path)

def __init_parser():
    event = ParserEvent()
    file_generator = FileGenerator()
    FileParser(event,file_generator)

def __application_start():
    Ignore.load()
    __init_parser()

def __application_execute():
    __do_generate()

def __application_end():
    pass

def main():
    __application_start()
    __application_execute()
    __application_end()
    return 0

if __name__ == '__main__':
    sys.exit(main())