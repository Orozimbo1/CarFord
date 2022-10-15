FROM python:3

COPY . /app

RUN pip install requirements.txt

WORKDIR /app

CMD [ "python", "app.py" ]