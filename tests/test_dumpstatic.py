#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os.path as path

from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

import django.contrib.admin as admin

class DumpStaticTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('dumpstatic', stdout=out)

        paths = [
            path.abspath('./tests'),
            '{}/static'.format(admin.__path__[0]),
        ]
        expected = json.dumps(paths)
        self.assertIn(expected, out.getvalue())


