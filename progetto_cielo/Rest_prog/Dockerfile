
# FROM python:3.9-slim
# WORKDIR /
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY server_p.py .
# EXPOSE 5004
# CMD ["python3", "server_p.py"]


# Usa un'immagine di base con Python
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /Rest_prog

# Copia il codice nell'immagine
COPY . /Rest_prog

# Installa le dipendenze
RUN pip install -r requirements.txt

# Esponi la porta sulla quale l'app ascolta
EXPOSE 5004

# Avvia l'app Flask
CMD ["python3", "server_p.py"]