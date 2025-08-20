# 🚀 Schritt-für-Schritt Deployment Guide

## Phase 1: Vorbereitung (30 Minuten)

### 1.1 GitHub Repository erstellen
```bash
# 1. Gehe zu github.com und erstelle ein neues privates Repository
# 2. Name: "restaurant-ki-agent"
# 3. Beschreibung: "KI-Agent für Restaurant Marketing Automatisierung"
```

### 1.2 Code hochladen
```bash
cd restaurant-ki-agent-production
git init
git add .
git commit -m "Initial commit - Restaurant KI-Agent MVP"
git branch -M main
git remote add origin https://github.com/IHR_USERNAME/restaurant-ki-agent.git
git push -u origin main
```

## Phase 2: Backend Deployment (45 Minuten)

### 2.1 Heroku Account & CLI Setup
```bash
# 1. Registrierung auf heroku.com
# 2. Heroku CLI installieren
# 3. Login: heroku login
```

### 2.2 Backend auf Heroku deployen
```bash
cd backend
echo "web: python src/main.py" > Procfile
echo "python-3.11.0" > runtime.txt

# Heroku App erstellen
heroku create restaurant-ki-agent-api

# Environment Variables setzen
heroku config:set OPENAI_API_KEY=your_actual_key_here
heroku config:set OPENAI_API_BASE=your_actual_base_url_here
heroku config:set FLASK_ENV=production

# PostgreSQL Datenbank hinzufügen
heroku addons:create heroku-postgresql:mini

# Code deployen
git add .
git commit -m "Add Procfile and runtime"
git push heroku main
```

### 2.3 Backend testen
```bash
# API URL: https://restaurant-ki-agent-api.herokuapp.com
curl https://restaurant-ki-agent-api.herokuapp.com/api/ai/test-connection
```

## Phase 3: Frontend Deployment (30 Minuten)

### 3.1 Vercel Account Setup
```bash
# 1. Registrierung auf vercel.com mit GitHub Account
# 2. Vercel CLI installieren: npm i -g vercel
```

### 3.2 Frontend konfigurieren
```bash
cd frontend
# .env.production Datei erstellen
echo "VITE_API_URL=https://restaurant-ki-agent-api.herokuapp.com" > .env.production
```

### 3.3 Frontend auf Vercel deployen
```bash
# Automatisches Deployment via GitHub Integration:
# 1. Vercel Dashboard öffnen
# 2. "New Project" klicken
# 3. GitHub Repository "restaurant-ki-agent" auswählen
# 4. Root Directory: "frontend"
# 5. Build Command: "pnpm run build"
# 6. Output Directory: "dist"
# 7. Environment Variables hinzufügen:
#    VITE_API_URL=https://restaurant-ki-agent-api.herokuapp.com
```

### 3.4 Frontend testen
```bash
# Dashboard URL: https://restaurant-ki-agent.vercel.app
# Teste alle Features im Browser
```

## Phase 4: Landing Page Deployment (15 Minuten)

### 4.1 Landing Page auf Netlify
```bash
# 1. Gehe zu netlify.com
# 2. Drag & Drop den "landing-page" Ordner
# 3. Oder GitHub Integration:
#    - "New site from Git"
#    - Repository auswählen
#    - Base directory: "landing-page"
#    - Build command: (leer lassen)
#    - Publish directory: "."
```

### 4.2 Custom Domain konfigurieren (Optional)
```bash
# 1. Domain bei Namecheap/GoDaddy kaufen
# 2. In Netlify: Site Settings > Domain Management
# 3. Custom Domain hinzufügen
# 4. DNS Records konfigurieren
```

## Phase 5: Finalisierung & Testing (30 Minuten)

### 5.1 End-to-End Test
```bash
# 1. Landing Page besuchen
# 2. Beta-Formular ausfüllen
# 3. Dashboard öffnen
# 4. Alle KI-Features testen:
#    - Social Media Post generieren
#    - Newsletter erstellen
#    - Menü optimieren
```

### 5.2 Performance & Monitoring
```bash
# Backend Logs überwachen:
heroku logs --tail -a restaurant-ki-agent-api

# Frontend Performance testen:
# - Google PageSpeed Insights
# - GTmetrix
```

## Phase 6: Go-Live Checklist

### ✅ Technische Checks
- [ ] Backend API erreichbar und funktionsfähig
- [ ] Frontend lädt ohne Fehler
- [ ] Landing Page responsive auf allen Geräten
- [ ] HTTPS aktiviert auf allen Domains
- [ ] CORS korrekt konfiguriert
- [ ] Environment Variables gesetzt
- [ ] Datenbank verbunden und migriert

### ✅ Business Checks
- [ ] Beta-Formular funktionsfähig
- [ ] E-Mail-Benachrichtigungen eingerichtet
- [ ] Pricing-Strategie definiert
- [ ] Terms of Service & Privacy Policy erstellt
- [ ] Google Analytics eingerichtet

### ✅ Marketing Checks
- [ ] Social Media Accounts erstellt
- [ ] SEO Meta-Tags optimiert
- [ ] Favicon und Branding konsistent
- [ ] Mobile Optimierung getestet

## 🎯 URLs nach Deployment

### Production URLs:
- **Landing Page:** https://restaurant-ki-agent.netlify.app
- **Dashboard:** https://restaurant-ki-agent.vercel.app  
- **Backend API:** https://restaurant-ki-agent-api.herokuapp.com

### Custom Domain Beispiele:
- **Landing Page:** https://www.restaurant-ki-agent.de
- **Dashboard:** https://app.restaurant-ki-agent.de
- **Backend API:** https://api.restaurant-ki-agent.de

## 💰 Monatliche Kosten

### Hosting:
- **Heroku (Backend):** $7/Monat (Hobby Plan)
- **Heroku Postgres:** $9/Monat (Mini Plan)
- **Vercel (Frontend):** $20/Monat (Pro Plan)
- **Netlify (Landing):** $0/Monat (Free Plan)

### APIs:
- **OpenAI GPT-4.1-mini:** ~$50-200/Monat (je nach Nutzung)

**Gesamt:** ~$86-216/Monat

## 🔧 Wartung & Updates

### Wöchentlich:
- Logs überprüfen
- Performance monitoren
- Backup-Status prüfen

### Monatlich:
- Dependencies aktualisieren
- Sicherheits-Updates installieren
- Kosten analysieren

### Bei Bedarf:
- Skalierung anpassen
- Features hinzufügen
- Bug-Fixes deployen

---

**Nach diesem Guide haben Sie ein vollständig funktionsfähiges, live geschaltetes Restaurant KI-Agent Business!** 🚀

