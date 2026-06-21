<<<<<<< HEAD
-%%writefile Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

=======
-%%writefile Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

>>>>>>> e65b3dc7ad11ab02ca25cd97cd70835292385881
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]