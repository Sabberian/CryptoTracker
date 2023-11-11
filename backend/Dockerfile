FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY . /backend

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]
