# main.py
from fastapi import FastAPI
from app.controllers.loan_controller import LoanController
from app.middlewares.cors_middleware import CORS

class App:
    def __init__(self):
        self.app = FastAPI()
        self.cors_middleware = CORS()
        self._configure_middlewares()
        self._configure_routes()

    def _configure_middlewares(self):
        self.cors_middleware.add(self.app)

    def _configure_routes(self):
        loan_controller = LoanController()

        self.app.include_router(loan_controller.router)

    def get_app(self):
        return self.app

app_instance = App()
app = app_instance.get_app()
