test:
	pytest

dev:
	PYTHONPATH=blockchain_interaction uvicorn api.main:app --reload
