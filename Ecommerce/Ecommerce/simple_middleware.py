def simple_middleware(get_response):

    def middleware(request):

        # forward going

        response = get_response(request)

        # backward going

        return response

    return middleware
