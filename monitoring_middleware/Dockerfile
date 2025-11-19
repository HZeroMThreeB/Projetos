FROM python:3.14.0-alpine3.22
 
WORKDIR /app
 
COPY requirements.txt .
 
RUN pip install -r requirements.txt

RUN mkdir dump_data
 
COPY alerts-route-api.py .
 
CMD ["uvicorn", "alerts-route-api:alertsMiddle", "--host", "0.0.0.0", "--port", "8000"]
