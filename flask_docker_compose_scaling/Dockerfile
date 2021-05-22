FROM python:3.8
LABEL maintainer="chunyenc"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python","app.py"]
