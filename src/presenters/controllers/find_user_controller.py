from src.domain.use_cases import FindUserInterface
from typing import Type
from src.presenters.helpers import HttpRequest,HttpResponse
from src.presenters.error import HttpErrors

class FindUserController:
    """class to define controller to find_user case"""

    def __init__(self,find_user_use_case:Type[FindUserInterface]) -> None:
        self.find_user_use_case=find_user_use_case

    def handle(self,http_request:Type[HttpRequest])->HttpResponse:
        """recieve htt_request end return http_response"""
        
        response=None
        if http_request.query:
            #if query
            
            query_string_params=http_request.query.keys()
            
            if "user_id" in query_string_params and "user_name" in query_string_params:
                user_id=http_request.query['user_id']
                user_name=http_request.query['user_name']
                response=self.find_user_use_case.by_id_and_name(user_id,user_name)
            
            elif "user_id" in query_string_params and "user_name" not in query_string_params:
                user_id=http_request.query['user_id']
                response=self.find_user_use_case.by_id(user_id)

            elif "user_id" not in query_string_params and "user_name" in query_string_params:
                user_name=http_request.query["user_name"]
                response=self.find_user_use_case.by_name(user_name)

            else:
            # caso de erros
                response={"Success":False,"Data":None}

            if response["Success"] is False:
                #apresentar o erro 422 em caso do usuario estar passando a query porém de o user_name ou user_id
                http_error=HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"],
                    body=http_error["body"]
                )
        
            return HttpResponse(
                status_code=200,
                body=response["Data"]
            )
    
        # if no query in http_request:
        http_error=HttpErrors.error_400()
        return HttpResponse(
            status_code=400,body=http_error["body"]
        )


