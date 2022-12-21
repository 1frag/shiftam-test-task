FROM python:3.10

COPY . /app

ENV PYTHONPATH=/app/blockchain_interaction

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0"]
