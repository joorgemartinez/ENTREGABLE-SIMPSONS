FROM python:3.9.12

COPY ./entregable_1.py /app/
COPY ./requirements.txt /app/
RUN mkdir General
RUN mkdir Homer
RUN mkdir Lisa

CMD ["python","entregable_1.py"]