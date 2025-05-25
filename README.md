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
```bash
git clone https://github.com/bruu-carmo/threat-intelligence-aggregator.git
cd threat-intelligence-aggregator
pip install -r requirements.txt
python main.py
