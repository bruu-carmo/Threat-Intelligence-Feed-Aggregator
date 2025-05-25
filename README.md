# Threat Intelligence Feed Aggregator

> **Empoderando analistas, desenvolvedores e defensores cibernéticos com dados de ameaças em tempo real.**

## 🚀 Funcionalidades
- Coleta de feeds de ameaças (AbuseIPDB, OTX, VirusTotal, ThreatFox)
- API REST para consultas
- Armazenamento em banco de dados (PostgreSQL ou SQLite)
- Exportação de dados em JSON e CSV
- Dashboard opcional com Streamlit
- Pipeline CI/CD com GitHub Actions
- Testes automatizados com pytest

---

## 🧠 Arquitetura
- Coletor de feeds → Banco → API → Dashboard / Exportação  
*(Veja o diagrama na pasta `/docs`)*

---

## 🗺️ Roadmap
- ✅ MVP: Coleta + API + Armazenamento
- 🔜 Dashboard
- 🔜 Alertas via Slack/Discord/Email
- 🔜 Machine Learning para enriquecimento de IOCs

---

## 🛠️ Tecnologias
- Python
- FastAPI
- PostgreSQL ou SQLite
- SQLAlchemy
- Requests
- Streamlit (opcional)
- GitHub Actions (CI/CD)
- Pytest

---

## ⚙️ Instalação

git clone https://github.com/bruu-carmo/threat-intelligence-aggregator.git
cd threat-intelligence-aggregator
pip install -r requirements.txt
python main.py

---

## 🧠 Executando a API
uvicorn threat_intelligence_aggregator.api:app --reload

> Acesse: http://127.0.0.1:8000/docs

---

## ✅ Testes
pytest

---

## 📜 Licença
MIT License