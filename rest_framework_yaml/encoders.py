"""
Helper classes for parsers.
"""
from __future__ import unicode_literals

import decimal
import types

from django.utils.encoding import force_str

from .compat import (
    Hyperlink,
    OrderedDict,
    ReturnDict,
    ReturnList,
    yaml,
    yaml_represent_text,
)


class SafeDumper(yaml.SafeDumper):
    """
    Handles decimals as strings.
    Handles OrderedDicts as usual dicts, but preserves field order, rather
    than the usual behaviour of sorting the keys.

    Adapted from http://pyyaml.org/attachment/ticket/161/use_ordered_dict.py
    """

    def represent_decimal(self, data):
        return self.represent_scalar("tag:yaml.org,2002:str", force_str(data))

    def represent_mapping(self, tag, mapping, flow_style=None):
        value = []
        node = yaml.MappingNode(tag, value, flow_style=flow_style)
        if self.alias_key is not None:
            self.represented_objects[self.alias_key] = node
        best_style = True
        if hasattr(mapping, "items"):
            mapping = list(mapping.items())
            if not isinstance(mapping, OrderedDict):
                mapping.sort()
        for item_key, item_value in mapping:
            node_key = self.represent_data(item_key)
            node_value = self.represent_data(item_value)
            if not (
                isinstance(node_key, yaml.ScalarNode) and not node_key.style
            ):
                best_style = False
            if not (
                isinstance(node_value, yaml.ScalarNode)
                and not node_value.style
            ):
                best_style = False
            value.append((node_key, node_value))
        if flow_style is None:
            if self.default_flow_style is not None:
                node.flow_style = self.default_flow_style
            else:
                node.flow_style = best_style
        return node


SafeDumper.add_representer(decimal.Decimal, SafeDumper.represent_decimal)

SafeDumper.add_representer(
    OrderedDict, yaml.representer.SafeRepresenter.represent_dict
)

SafeDumper.add_representer(
    types.GeneratorType, yaml.representer.SafeRepresenter.represent_list
)

if Hyperlink:
    SafeDumper.add_representer(Hyperlink, yaml_represent_text)

if ReturnDict:
    SafeDumper.add_representer(
        ReturnDict, yaml.representer.SafeRepresenter.represent_dict
    )

if ReturnList:
    SafeDumper.add_representer(
        ReturnList, yaml.representer.SafeRepresenter.represent_list
    )
