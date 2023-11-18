FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY . /backend

RUN python3 -m pip install --upgrade pip --progress-bar off

RUN pip install -r ./requirements.txt --progress-bar off

CMD ["python", "./main.py"]
