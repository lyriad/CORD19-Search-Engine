FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]