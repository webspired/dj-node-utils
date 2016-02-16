# -*- coding: utf-8 -*-
import json

from django.core.management import BaseCommand

from ...import get_static_paths

class Command (BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(json.dumps(get_static_paths()))
