FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY . /app/

ENTRYPOINT ["python3"]

CMD ["/app/MINI_PROJECT.py"]