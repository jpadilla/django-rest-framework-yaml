# Parsers

## Setting the parsers

The default set of parsers may be set globally, using the `DEFAULT_PARSER_CLASSES` setting.  For example, the following settings would allow requests with `YAML` content.

    REST_FRAMEWORK = {
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.YAMLParser',
        )
    }

You can also set the parsers used for an individual view, or viewset,
using the `APIView` class based views.

    from rest_framework.parsers import YAMLParser
    from rest_framework.response import Response
    from rest_framework.views import APIView

    class ExampleView(APIView):
        """
        A view that can accept POST requests with YAML content.
        """
        parser_classes = (YAMLParser,)

        def post(self, request, format=None):
            return Response({'received data': request.DATA})

Or, if you're using the `@api_view` decorator with function based views.

    @api_view(['POST'])
    @parser_classes((YAMLParser,))
    def example_view(request, format=None):
        """
        A view that can accept POST requests with YAML content.
        """
        return Response({'received data': request.DATA})

---

# API Reference

## YAMLParser

Parses `YAML` request content.

Requires the `pyyaml` package to be installed.

**.media_type**: `application/yaml`
