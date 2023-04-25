

class A:
    def __init__(self,name,idade) -> None:
        self.name=name
        self.idade=idade


marcelo=A(name="marcelo",idade=26)
query_data=None
# data={"name":'marcelo','idade':26}




query_data=[marcelo]

print(type(query_data))