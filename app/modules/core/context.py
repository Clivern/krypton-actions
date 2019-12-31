# Copyright 2019 Silverbackhq
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Local Library
from app.modules.entity.option_entity import OptionEntity


class Context():

    def __init__(self):
        self.__data = {}
        self.__option_entity = OptionEntity()

    def push(self, new_data):
        self.__data.update(new_data)

    def load_options(self, options):
        options_to_load = {}
        for key in options.keys():
            options_to_load[key] = options[key]
            if key not in self.__data.keys():
                self.__data[key] = options[key]

        if len(options_to_load.keys()) > 0:
            new_options = self.__option_entity.get_many_by_keys(options_to_load.keys())
            for option in new_options:
                self.__data[option.key] = option.value

    def autoload_options(self):
        options = self.__option_entity.get_many_by_autoload(True)
        for option in options:
            self.__data[option.key] = option.value

    def get(self, key=None, default=None):
        if key is not None:
            return self.__data[key] if key in self.__data else default
        return self.__data
