<div class="badges">
    <a href="http://travis-ci.org/jpadilla/django-rest-framework-yaml?branch=master">
        <img src="https://travis-ci.org/jpadilla/django-rest-framework-yaml.svg?branch=master">
    </a>
    <a href="https://pypi.python.org/pypi/djangorestframework-yaml">
        <img src="https://pypip.in/version/djangorestframework-yaml/badge.svg">
    </a>
</div>

---

# REST Framework YAML

YAML support for Django REST Framework

---

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

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
$ pip install -r requirements-test.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```


[pyyaml]: http://pyyaml.org/
