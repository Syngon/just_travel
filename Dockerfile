FROM python:3.10

RUN mkdir -p /code
WORKDIR /code
RUN pip install --upgrade pip

COPY ./requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY ./src /code/
COPY ./models.db /code/
COPY ./dev.sqlite3.db /code/
expose 8000

# python -m uvicorn src.server:app --reload
CMD ["uvicorn", "src.server:app", "--host", "127.0.0.1", "--port", "8000"]
