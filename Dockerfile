FROM python:3.12.3-slim
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY ./my_app/ /app/
EXPOSE 5000
ENV FLASK_APP=__init__.py
CMD ["flask", "run", "--host", "0.0.0.0"]
