from src.presentation.controllers.controle_create_controler import (
    ControleCreateController,
)
from src.repository.repo_atleta import AtletaRepo
from src.repository.repo_clube import ClubeRepo
from src.use_cases.clube_create import ClubeCreateUseCase


def clube_create_composer(data: dict, session):
    clube_repository = ClubeRepo(session)
    atleta_repository = AtletaRepo(session)

    use_case = ClubeCreateUseCase(
        clube_repository=clube_repository,
        atleta_repository=atleta_repository,
    )
    controller = ControleCreateController(use_case=use_case)

    return controller.handle(data)
