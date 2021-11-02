from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
class JWTVerifyTokenMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Called just before Django calls the view.
        """
        view_name = '.'.join((view_func.__module__, view_func.__name__))
        print('view')
        print(view_name)
        # If the view name is in our exclusion list, exit early
        exclusion_set = getattr(settings, 'EXCLUDE_FROM_MY_MIDDLEWARE', set())
        print(exclusion_set)
        if view_name in exclusion_set:
         print(view_name)
         return view_name
        print("varun")
        print(request.headers['Authorization'])
        token=request.headers['Authorization']
        data = {'token': token}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        print(valid_data)
        user = valid_data['user']
        return user

    def process_exception(self, request, exception):
        """
        Called when a view raises an exception.
        """
        return exception

    def process_template_response(self, request, response):
        """
        Called just after the view has finished executing.
        """
        return response