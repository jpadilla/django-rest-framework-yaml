"""
Provides YAML parsing support.
"""
from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import force_str
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser

from .compat import yaml


class YAMLParser(BaseParser):
    """
    Parses YAML-serialized data.
    """

    media_type = "application/yaml"

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as YAML and returns the resulting data.
        """
        assert yaml, "YAMLParser requires pyyaml to be installed"

        parser_context = parser_context or {}
        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return yaml.safe_load(data)
        except (ValueError, yaml.parser.ParserError) as exc:
            raise ParseError("YAML parse error - %s" % force_str(exc))
