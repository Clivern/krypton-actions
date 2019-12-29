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

# Standard Library
import os
from importlib import import_module

# Third Party Library
from celery import Celery
from celery.signals import task_success

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery('app')

# namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@task_success.connect
def after_task(sender=None, result=None, **kwargs):
    if sender.request.id and "status" in result and "result" in result:
        task_module = import_module("app.modules.core.task")
        task_class = getattr(task_module, "Task")

        task_class().update_task_with_uuid(
            sender.request.id,
            {
                "status": result["status"],
                "result": result["result"]
            }
        )
