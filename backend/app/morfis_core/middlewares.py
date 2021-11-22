from threading import local

# Global thread-safe variable
_user = local()

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        self.process_request(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    # def process_exception(self, request, exception):
    #     _user.value = None
    #
    # def process_template_response(self, request, response):
    #     _user.value = None
    #     return response

    def process_request(self, request):
        _user.value = request.user

    @staticmethod
    def get_current_user():
        if hasattr(_user, 'value') and _user.value:
            return _user.value