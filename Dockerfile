# Verwenden Sie ein offizielles Python-Runtime-Image als Basis
FROM python:3.9-slim

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie die Anforderungen-Datei in das Arbeitsverzeichnis
COPY requirements.txt .

# Installieren Sie die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren Sie den Rest des Anwendungscodes
COPY . .

# Exponieren Sie den Port, auf dem die App läuft
EXPOSE 8000

# Startbefehl für die Anwendung
CMD ["python", "index.py"]
