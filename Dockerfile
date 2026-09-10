# Použijeme oficiální odlehčený obraz Pythonu
FROM python:3.10-slim

# Zabráníme Pythonu vytvářet zbytečné .pyc soubory a zajistíme výpis logů
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Vytvoříme pracovní složku v kontejneru
WORKDIR /app

# Zkopírujeme soubor s požadavky a nainstalujeme závislosti
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Zkopírujeme zbytek tvého kódu
COPY . /app/

# Řekneme Dockeru, na kterém portu aplikace poběží
EXPOSE 8000

# Příkaz, který aplikaci reálně spustí (včetně automatické migrace databáze)
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]