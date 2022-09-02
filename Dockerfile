FROM python:alpine3.15
ADD ./app ./app
WORKDIR /app
RUN pip install -r ./app/requirements.txt
ENTRYPOINT [ "python", "-u", "./app/app.py" ]