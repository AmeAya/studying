def check_fields(required_fields):
    from rest_framework.response import Response
    from rest_framework.status import HTTP_400_BAD_REQUEST
    def decorator(view):
        def wrapper(self, request, *args, **kwargs):
            for field in required_fields:
                if field not in request.data:
                    return Response(data={'message': f'Field "{field}" is required!'}, status=HTTP_400_BAD_REQUEST)
            return view(self, request, *args, **kwargs)
        return wrapper
    return decorator
