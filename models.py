from pydantic import BaseModel


class OperationRequest(BaseModel):

    a: float
    b: float

class OperationRequest2(BaseModel):

    a: float


class OperationResponse(BaseModel):
    """
    Modelo de dados para representar a resposta de uma operação matemática.

    Atributos:
        result (float): O resultado da operação matemática realizada.
    """
    result: float
