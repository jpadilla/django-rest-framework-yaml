# Renderers

## Setting the renderers

The default set of renderers may be set globally, using the `DEFAULT_RENDERER_CLASSES` setting.  For example, the following settings would use `YAML` as the main media type and also include the self describing API.

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.YAMLRenderer',
        )
    }

You can also set the renderers used for an individual view, or viewset,
using the `APIView` class based views.

    from django.contrib.auth.models import User
    from rest_framework.renderers import YAMLRenderer
    from rest_framework.response import Response
    from rest_framework.views import APIView

    class UserCountView(APIView):
        """
        A view that returns the count of active users, in JSON or YAML.
        """
        renderer_classes = (YAMLRenderer,)

        def get(self, request, format=None):
            user_count = User.objects.filter(active=True).count()
            content = {'user_count': user_count}
            return Response(content)

Or, if you're using the `@api_view` decorator with function based views.

    @api_view(['GET'])
    @renderer_classes((YAMLRenderer,))
    def user_count_view(request, format=None):
        """
        A view that returns the count of active users, in JSON or JSONp.
        """
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)

---

# API Reference

## YAMLRenderer

Renders the request data into `YAML`.

Requires the `pyyaml` package to be installed.

Note that non-ascii characters will be rendered using `\uXXXX` character escape.  For example:

    unicode black star: "\u2605"

**.media_type**: `application/yaml`

**.format**: `'.yaml'`

**.charset**: `utf-8`
