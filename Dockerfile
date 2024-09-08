
FROM python:3.10

ADD . /sandbox


WORKDIR /sandbox

COPY . /sandbox

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "../app.py"]
