# Restaurant KI-Agent - Production Deployment Guide

## 🚀 Übersicht

Dieses Repository enthält den vollständigen Code für das Restaurant KI-Agent Business:
- **Backend API** (Flask + OpenAI Integration)
- **Frontend Dashboard** (React + Tailwind CSS)  
- **Landing Page** (HTML + Tailwind CSS)
- **Deployment Dokumentation**

## 📁 Projektstruktur

```
restaurant-ki-agent-production/
├── backend/                 # Flask API Server
│   ├── src/
│   │   ├── routes/         # API Endpoints
│   │   ├── models/         # Datenbank Modelle
│   │   └── main.py         # Hauptanwendung
│   ├── venv/               # Python Virtual Environment
│   └── requirements.txt    # Python Dependencies
├── frontend/               # React Dashboard
│   ├── src/
│   │   ├── components/     # React Komponenten
│   │   └── App.jsx         # Hauptkomponente
│   ├── public/
│   └── package.json        # Node.js Dependencies
├── landing-page/           # Marketing Website
│   └── index.html          # Statische Landing Page
├── docs/                   # Dokumentation
└── README.md               # Diese Datei
```

## 🔧 Lokale Entwicklung

### Backend starten:
```bash
cd backend
source venv/bin/activate
python src/main.py
# Läuft auf http://localhost:5000
```

### Frontend starten:
```bash
cd frontend
pnpm install
pnpm run dev --host
# Läuft auf http://localhost:5173
```

### Landing Page:
```bash
cd landing-page
# Öffne index.html im Browser oder verwende einen lokalen Server
```

## 🌐 Production Deployment

### 1. Backend Deployment (Heroku/Render)

**Heroku Deployment:**
```bash
# In backend/ Verzeichnis
echo "web: python src/main.py" > Procfile
git init
git add .
git commit -m "Initial commit"
heroku create ihr-restaurant-api
heroku config:set OPENAI_API_KEY=your_key_here
heroku config:set OPENAI_API_BASE=your_base_url_here
git push heroku main
```

**Render Deployment:**
1. Repository auf GitHub pushen
2. Render.com Account erstellen
3. "New Web Service" wählen
4. GitHub Repository verbinden
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `python src/main.py`
7. Environment Variables setzen:
   - `OPENAI_API_KEY`
   - `OPENAI_API_BASE`

### 2. Frontend Deployment (Vercel/Netlify)

**Vercel Deployment:**
```bash
# In frontend/ Verzeichnis
npm install -g vercel
vercel
# Folge den Anweisungen
```

**Netlify Deployment:**
1. Repository auf GitHub pushen
2. Netlify Account erstellen
3. "New site from Git" wählen
4. GitHub Repository verbinden
5. Build Command: `pnpm run build`
6. Publish Directory: `dist`

### 3. Landing Page Deployment

**Netlify (Empfohlen):**
1. Drag & Drop der `landing-page/` Ordner auf netlify.com
2. Oder GitHub Integration wie beim Frontend

## 🔐 Umgebungsvariablen

### Backend (.env Datei):
```
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=your_openai_base_url
FLASK_ENV=production
SECRET_KEY=your_secret_key_here
```

### Frontend:
```
VITE_API_URL=https://ihr-backend-url.herokuapp.com
```

## 🗄️ Datenbank Setup

Für Production wird eine echte Datenbank benötigt:

**PostgreSQL (Heroku/Render):**
```python
# In backend/src/main.py
import os
DATABASE_URL = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
```

## 📊 Monitoring & Analytics

### Backend Monitoring:
- **Heroku:** Integrierte Logs und Metriken
- **Render:** Dashboard mit Performance Daten
- **Sentry:** Für Error Tracking

### Frontend Analytics:
- **Google Analytics:** Für Nutzerverhalten
- **Hotjar:** Für Heatmaps und Session Recordings

## 🔒 Sicherheit

### API Sicherheit:
- Rate Limiting implementieren
- CORS korrekt konfigurieren
- API Keys sicher verwalten
- HTTPS erzwingen

### Frontend Sicherheit:
- Environment Variables für API URLs
- Content Security Policy
- XSS Protection

## 💰 Kosten Übersicht

### Hosting Kosten (monatlich):
- **Backend (Heroku Hobby):** $7/Monat
- **Frontend (Vercel Pro):** $20/Monat
- **Landing Page (Netlify):** Kostenlos
- **Datenbank (Heroku Postgres):** $9/Monat
- **Domain:** ~$12/Jahr

**Gesamt:** ~$36/Monat für vollständige Infrastruktur

### OpenAI API Kosten:
- **GPT-4.1-mini:** ~$0.15 pro 1K Tokens
- **Geschätzt:** $50-200/Monat je nach Nutzung

## 🚀 Go-Live Checklist

### Vor dem Launch:
- [ ] Backend auf Heroku/Render deployed
- [ ] Frontend auf Vercel/Netlify deployed  
- [ ] Landing Page live geschaltet
- [ ] Domain konfiguriert
- [ ] SSL Zertifikate aktiv
- [ ] Environment Variables gesetzt
- [ ] Datenbank migriert
- [ ] API Endpoints getestet
- [ ] Cross-Origin Requests funktionieren
- [ ] Monitoring eingerichtet
- [ ] Backup-Strategie implementiert

### Nach dem Launch:
- [ ] Google Analytics eingerichtet
- [ ] SEO optimiert
- [ ] Social Media Accounts erstellt
- [ ] Erste Beta-Kunden kontaktiert
- [ ] Feedback-System implementiert

## 📞 Support & Wartung

### Regelmäßige Aufgaben:
- **Wöchentlich:** Logs überprüfen, Performance monitoren
- **Monatlich:** Dependencies aktualisieren, Sicherheits-Updates
- **Quartalsweise:** Backup-Tests, Disaster Recovery Tests

### Skalierung:
- **Backend:** Heroku Dynos hochskalieren oder zu AWS/GCP migrieren
- **Frontend:** Vercel Pro Features nutzen oder CDN implementieren
- **Datenbank:** PostgreSQL Plan upgraden oder Sharding implementieren

## 🎯 Nächste Schritte

1. **GitHub Repository erstellen** und Code hochladen
2. **Hosting-Accounts** bei Heroku/Render und Vercel/Netlify erstellen
3. **Domain registrieren** (z.B. restaurant-ki-agent.de)
4. **Deployment durchführen** nach dieser Anleitung
5. **Beta-Programm starten** mit der Live-Landing-Page

---

**Entwickelt für maximale Skalierbarkeit und Wartbarkeit.**
**Bereit für den Einsatz mit echten Kunden und echtem Revenue.**

