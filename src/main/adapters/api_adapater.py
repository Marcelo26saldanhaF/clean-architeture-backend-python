from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface
from src.presenters.helpers import HttpRequest,HttpResponse
from src.presenters.error import HttpErrors

def flask_adapter(request:any,api_route:Type[RouteInterface])->any:
    """Adapter pttern to flask
        :params - flask request
        :api_route- compose routes
    """
    http_request=HttpRequest(body=request.get_json())
    try:
        response=api_route.route(http_request)
    except IntegrityError:
        http_error=HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error['status_code'],
            body=http_error['body']
        )
    return response
    
    


    