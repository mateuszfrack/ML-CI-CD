# Oparcie na lekkim, oficjalnym obrazie Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie pliku z bibliotekami i ich instalacja
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiowanie reszty plików aplikacji (w tym app.py)
COPY . .

# Wystawienie portu 8000 na zewnątrz kontenera
EXPOSE 8000

# Komenda uruchamiająca serwer FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]