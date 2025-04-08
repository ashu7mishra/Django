class SimpleClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # This is before
        print("This is before for class based middleware")
        response = self.get_response(request)
        print("This is after for class based middleware")
        # This is after
        return response
