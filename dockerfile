FROM python:3.9.12

COPY ./entregable_1.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/
RUN mkdir General
RUN mkdir Homer
RUN mkdir Lisa
RUN pip install -r requirements.txt

CMD ["python","entregable_1.py"]

