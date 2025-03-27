class SimpleClassMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # This is before
        response = self.get_response(request)
        # This is after
        return response
