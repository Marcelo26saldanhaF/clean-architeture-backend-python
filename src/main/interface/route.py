from abc import ABC,abstractmethod
from ...presenters.helpers import HttpRequest,HttpResponse
from typing import Type

class RouteInterface(ABC):
    """Interface to Routes"""
    @abstractmethod
    def route(self,http_request:Type[HttpRequest])->HttpResponse:
        """Define Route"""
        raise Exception("method must be implemented")