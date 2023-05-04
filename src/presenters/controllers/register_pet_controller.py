from typing import Type,Dict
from src.domain.use_cases import RegisterPetInterface
from src.presenters.helpers import HttpRequest,HttpResponse
from src.presenters.error import HttpErrors
from src.main.interface import RouteInterface

class RegisterPetController(RouteInterface):
    """Class to controller use case register pet"""

    def __init__(self,register_pet_use_case:Type[RegisterPetInterface]) -> None:
        self.register_pet_use_case=register_pet_use_case

    def route(self,http_request:Type[HttpRequest])->HttpResponse:
        """"""
        response=None
        if http_request.body:
            # if exist something inside body
            body_params=http_request.body.keys()

            if "name" in body_params and "specie" in body_params and "user_information" in body_params:
                user_information_params=http_request.body['user_information'].keys()
                if "user_name" in user_information_params or "user_id" in user_information_params:

                    name=http_request.body['name']
                    specie=http_request.body['specie']
                    user_information=http_request.body['user_information'] 

                    if "age" in body_params:
                        age=http_request.body['age']
                    else:
                        age=None

                    response=self.register_pet_use_case.register(name=name,specie=specie,user_information=user_information,age=age)

                else:
                    response={'Success':False,'Data':None}    
            else:
                response={'Success':False,'Data':None}

            if response['Success'] is False:
                http_error=HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error['status_code'],
                    body=http_error['body']
                )   
            return HttpResponse(
                status_code=200,body=response['Data']
            )
        
        else:
            http_error=HttpErrors.error_400()
            return HttpResponse(
                status_code=http_error['status_code'],
                body=http_error['body']
            )

    

        