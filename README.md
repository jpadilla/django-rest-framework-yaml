# REST Framework YAML

[![build-status-image]][travis]
[![pypi-version]][pypi]

## Overview

YAML support extracted as a third party package directly from the official Django REST Framework implementation. It's built using the [PyYAML][pyyaml] package.

## Requirements

* Python (2.7, 3.3, 3.4)
* Django (1.6, 1.7)

## Installation

Install using `pip`...

```bash
$ pip install djangorestframework-yaml
```

## Example

```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_yaml.parsers.YAMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_yaml.renderers.YAMLRenderer',
    ),
}
```

You can also set the renderer and parser used for an individual view, or viewset, using the APIView class based views.

```python
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_yaml.parsers import YAMLParser
from rest_framework_yaml.renderers import YAMLRenderer

class ExampleView(APIView):
    """
    A view that can accept POST requests with YAML content.
    """
    parser_classes = (YAMLParser,)
    renderer_classes = (YAMLRenderer,)

    def post(self, request, format=None):
        return Response({'received data': request.DATA})
```

## Documentation & Support

Full documentation for the project is available at http://jpadilla.github.io/django-rest-framework-yaml/.

You may also want to follow the [author][jpadilla] on Twitter.


[build-status-image]: https://secure.travis-ci.org/jpadilla/django-rest-framework-yaml.png?branch=master
[travis]: http://travis-ci.org/jpadilla/django-rest-framework-yaml?branch=master
[pypi-version]: https://pypip.in/version/djangorestframework-yaml/badge.svg
[pypi]: https://pypi.python.org/pypi/djangorestframework-yaml
[pyyaml]: http://pyyaml.org/
[jpadilla]: https://twitter.com/jpadilla_
