from typing import Type
from src.domain.use_cases import RegisterUserInterface
from src.presenters.helpers import HttpRequest,HttpResponse
from src.presenters.error import HttpErrors
from src.main.interface import RouteInterface



class RegisterUserController(RouteInterface):
    """Class to controll register user case """

    def __init__(self,register_user_case:Type[RegisterUserInterface]) -> None:
        self.register_user_case=register_user_case

    def route(self,http_request:Type[HttpRequest])->HttpResponse:
        """class to define route"""
        response=None
        if http_request.body:
            user_params=http_request.body.keys()
            if "name" in user_params and "password" in user_params:
                response=self.register_user_case.register(name=http_request.body['name'],password=http_request.body['password'])

                if response['Success']:
                    return HttpResponse(
                        status_code=200,
                        body=response['Data']
                    )
                else:
                     response={"Success":False,"Data":None}
            
            else:
                 response={"Success":False,"Data":None} 

            if response['Success'] is False:   
                http_erro=HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_erro['status_code'],
                    body=http_erro['body']
                )

        else:
            http_erro=HttpErrors.error_400()
            return HttpResponse(
                status_code=http_erro['status_code'],
                body=http_erro['body']
            )        
            

