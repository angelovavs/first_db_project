FROM python:3.10.2-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat
RUN pip install --user --upgrade aws-sam-cli 
RUN pip install --upgrade pip
RUN pip install SQLAlchemy
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

RUN ["/bin/bash", "-c", "echo before copy"]
COPY . /usr/src/app/
RUN ["/bin/bash", "-c", "echo after copy; ls -lh"]

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

