from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterUserController
from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import User_repository


def register_user_compose()->RouteInterface:
    """Composing Register User Route
        :params - None
        :return - Object with register user Routes
    """
    repository=User_repository()
    use_case=RegisterUser(repository)
    register_user_route=RegisterUserController(use_case)

    return register_user_route

