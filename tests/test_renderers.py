# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal

from django.test import TestCase
from rest_framework.compat import BytesIO
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_yaml.parsers import YAMLParser


_yaml_repr = 'foo: [bar, baz]\n'


class YAMLRendererTests(TestCase):
    """
    Tests specific to the YAML Renderer
    """

    def test_render(self):
        """
        Test basic YAML rendering.
        """
        obj = {'foo': ['bar', 'baz']}
        renderer = YAMLRenderer()
        content = renderer.render(obj, 'application/yaml')
        self.assertEqual(content.decode('utf-8'), _yaml_repr)

    def test_render_and_parse(self):
        """
        Test rendering and then parsing returns the original object.
        IE obj -> render -> parse -> obj.
        """
        obj = {'foo': ['bar', 'baz']}

        renderer = YAMLRenderer()
        parser = YAMLParser()

        content = renderer.render(obj, 'application/yaml')
        data = parser.parse(BytesIO(content))
        self.assertEqual(obj, data)

    def test_render_decimal(self):
        """
        Test YAML decimal rendering.
        """
        renderer = YAMLRenderer()
        content = renderer.render({'field': Decimal('111.2')}, 'application/yaml')
        self.assertYAMLContains(content.decode('utf-8'), "field: '111.2'")

    def assertYAMLContains(self, content, string):
        self.assertTrue(string in content, '%r not in %r' % (string, content))

    def test_proper_encoding(self):
        obj = {'countries': ['United Kingdom', 'France', 'España']}
        renderer = YAMLRenderer()
        content = renderer.render(obj, 'application/yaml')
        self.assertEqual(content.strip(), 'countries: [United Kingdom, France, España]'.encode('utf-8'))
