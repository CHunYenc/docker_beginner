FROM python:3.8
LABEL maintainer="value"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3","flask run"]