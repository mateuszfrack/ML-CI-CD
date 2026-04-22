# ML API - Laboratorium 04

Aplikacja serwująca model regresji liniowej (y = 2x + 1) zbudowana przy użyciu FastAPI i skonteneryzowana za pomocą Dockera.

## Instrukcja uruchamiania

### 1. Lokalnie (Python)
Wymagany Python 3.9+.
1. Zainstaluj biblioteki: `pip install -r requirements.txt`
2. Uruchom serwer: `uvicorn app:app --host 0.0.0.0 --port 8000`

### 2. Za pomocą Docker
1. Zbuduj obraz: `docker build -t ml-api-image .`
2. Uruchom kontener: `docker run -d -p 8000:8000 ml-api-image`

### 3. Za pomocą Docker Compose (Zalecane)
Wystarczy jedna komenda, aby uruchomić API wraz z bazą danych Redis:
`docker-compose up -d`

## Konfiguracja i zasoby
- **Porty:** Aplikacja domyślnie nasłuchuje na porcie `8000`.
- **Sieć:** Kontenery komunikują się wewnątrz sieci `ml-network`.
- **Zasoby:** Minimalne wymagania (ok. 100-200MB RAM).