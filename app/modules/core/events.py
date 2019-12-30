# Copyright 2019 Clivern
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


class Events():

    def __init__(self):
        self.events = {}

    def declare_event(self, event_name):
        self.events[event_name] = []

    def push_handler(self, event_name, handler):
        if event_name in self.events.keys():
            self.events[event_name].append(handler)
        else:
            self.events[event_name] = [handler]

    def get_handlers(self, event_name):
        return self.events[event_name]

    def get_events(self):
        return self.events.keys()

    def count_handlers(self, event_name):
        return len(self.events[event_name])

    def run(self, event_name, payload, **args):
        for handler in self.get_handlers(event_name):
            handler.run(payload, **args)
