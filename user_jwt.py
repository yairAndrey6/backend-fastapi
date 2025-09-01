import jwt 

# Creación del token para inicio de sesión
def create_token(data: dict):
    token : str = jwt.encode(payload=data, key="mysecretkey",algorithm="HS256")
    return token

# Validación de Token
def validate_token(token: str) -> dict:
    data :dict = jwt.decode(token,key="mysecretkey",algorithms="HS256")
    return data
