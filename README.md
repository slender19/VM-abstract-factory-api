para ejecutar:

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000

luego abren: http://127.0.0.1:8000/docs
