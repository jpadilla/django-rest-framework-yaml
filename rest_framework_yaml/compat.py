"""
The `compat` module provides support for backwards compatibility with older
versions of django/python, and compatibility wrappers around optional packages.
"""
# flake8: noqa

try:
    import yaml
except ImportError:
    yaml = represent_text = None
else:
    yaml_represent_text = yaml.representer.SafeRepresenter.represent_str

# OrderedDict only available in Python 2.7.
# This will always be the case in Django 1.7 and above, as these versions
# no longer support Python 2.6.
# For Django <= 1.6 and Python 2.6 fall back to SortedDict.
try:
    from collections import OrderedDict
except:
    from django.utils.datastructures import SortedDict as OrderedDict

try:
    # Note: Hyperlink is private(?) API from DRF 3
    from rest_framework.relations import Hyperlink
except ImportError:
    Hyperlink = None

try:
    # Note: ReturnDict and ReturnList are private API from DRF 3
    from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
except ImportError:
    ReturnDict = None
    ReturnList = None
