def simple_middleware(get_response):

    def middleware(request):

        # forward going
        print("THis is before health check")
        response = get_response(request)
        print("THis is after health check")

        # backward going

        return response

    return middleware


def another_middleware(get_response):

    def middleware(request):

        # forward going
        print("THis is before health but after simple middleware check")
        response = get_response(request)
        print("THis is after health and after simple middleware check")

        # backward going

        return response

    return middleware
