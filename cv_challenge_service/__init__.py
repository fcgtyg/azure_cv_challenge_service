import logging

import azure.functions as func
from .api import app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)
