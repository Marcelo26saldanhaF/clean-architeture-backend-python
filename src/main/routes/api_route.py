from flask import Blueprint,jsonify,request
from src.main.compose import register_user_compose,register_pet_composer
from src.main.adapters import flask_adapter

api_routes_bp=Blueprint('api_routes',__name__)

@api_routes_bp.route("/api/users",methods=["POST",])
def register_user():
    """register user route"""
    message=None
    response=flask_adapter(request=request,api_route=register_user_compose())
    print(response.status_code)
    if response.status_code <300:
        message={
            "type":"users",
            "id": response.body.id,
            "attributes":{"name":response.body.name}
        }
        
        return  jsonify({"data":message}),response.status_code
    
    return jsonify({"error":{"status":response.status_code,
            "title":response.body['error']}
            }),response.status_code


@api_routes_bp.route("/api/pets",methods=["POST",])
def register_pets():
    """register pet route"""
    mensage=None
    response=flask_adapter(request=request,api_route=register_pet_composer())
    print(response.status_code)
    if response.status_code <300:
        message={
            "type":"pets",
            "id": response.body.id,
            "attributes":{"name":response.body.name,
                        #   "specie":response.body.specie, resolver esse problema pois o objeto não é serealizavel
                          "age":response.body.age
                          },
            "relationships":{"owner":{
                "type":"users",
                "id":response.body.user_id
            }}
        }
        
        return  jsonify({"data":message}),response.status_code
    
    return jsonify({"error":{"status":response.status_code,
            "title":response.body['error']}
            }),response.status_code

