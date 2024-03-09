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

from utility import open_file_w,create_dir
from constants import UTF8,IMPORT_SYS,MAIN_FUNCTION,PY_ENTRY

class FileWriteMixin:
    """
    The FileWriteMixin would be a template class for generating templated data.
    """
    @staticmethod
    def write_file_with_template(file_path, content):
        try:
            create_dir(file_path)
            file = open_file_w(file_path, UTF8)
            file.write(f"# {content}")
            file.write('\n' * 2)
            file.write(IMPORT_SYS)
            file.write('\n' * 10)
            file.write(MAIN_FUNCTION)
            file.write('\n' * 2)
            file.write(PY_ENTRY)
        except Exception as e:
            print(f"Write File error, file={file_path}, e={e}")
        finally:
            file.close()