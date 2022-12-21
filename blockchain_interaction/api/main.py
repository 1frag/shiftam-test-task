import json
import logging

from fastapi import FastAPI, Request, Response

from api.handlers import v1

app = FastAPI()

app.include_router(v1.router)


@app.middleware('http')
async def handle_unexpected_error(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as error:
        logging.error('Unexpected server error', extra={'error': error})
        return Response(
            content=json.dumps({
                'error': 'Internal server error',
            }),
            status_code=500,
        )
