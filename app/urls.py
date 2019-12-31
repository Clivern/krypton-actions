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

from django.urls import include, path

# Local Library
from app.controllers.web.home import Home
from app.controllers.api.github.authorization import Authorization
from app.controllers.api.github.webhook import Webhook
from app.controllers.api.github.setup import Setup
from app.controllers.web.not_found import handler404 as handler404_view
from app.controllers.web.error import handler500 as handler500_view

urlpatterns = [
    path('', Home.as_view(), name='app.web.home'),

    path('api/github/', include([
        path('authorization', Authorization.as_view(), name='app.api.github.authorization.endpoint'),
        path('webhook', Webhook.as_view(), name='app.api.github.webhook.endpoint'),
        path('setup', Setup.as_view(), name='app.api.github.setup.endpoint'),
    ]))
]

handler404 = handler404_view
handler500 = handler500_view
