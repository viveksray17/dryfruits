FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV DEBUG="false" PORT=5000 HOST="0.0.0.0"
EXPOSE 5000
CMD [ "python", "app.py" ]
COPY . .
