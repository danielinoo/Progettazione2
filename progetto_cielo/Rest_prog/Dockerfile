
FROM python:3.9-slim
WORKDIR /server_p
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY server_p.py .
EXPOSE 8085
CMD ["python3", "server_p.py"]