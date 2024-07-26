from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import (
    HttpResponse,
    HttpStatusCode,
)
from src.presentation.interfaces.controller_interface import (
    ControllerInterface,
)
from src.use_cases.usuario_update_password import UsuarioUpdatePasswordUseCase


class UsuarioUpdatePasswordController(ControllerInterface):
    def __init__(self, use_case: UsuarioUpdatePasswordUseCase):
        self._use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        result: list = self._use_case.execute(http_request=http_request)

        return HttpResponse(body=result, status_code=HttpStatusCode.OK.value)
