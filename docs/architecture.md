# 🧠 Arquitetura – Threat Intelligence Feed Aggregator

## 🔥 Componentes

1. **Feed Collectors:** 
   - Conecta nos APIs públicos (AbuseIPDB, OTX, ThreatFox, VirusTotal)
   - Faz parse e normaliza dados
   - Salva no banco (PostgreSQL ou SQLite)

2. **Database:** 
   - Armazena IOCs normalizados
   - Suporta consultas rápidas

3. **API REST (FastAPI):** 
   - /status → Status da API
   - /feeds → Lista de feeds ativos
   - /lookup/{ioc} → Pesquisa de IOC

4. **Dashboard (Opcional):** 
   - Interface visual em Streamlit

5. **Exportação:** 
   - JSON e CSV direto da API ou da interface

6. **Pipeline CI/CD:** 
   - GitHub Actions → Testes, build, lint e deploy

---

## 🔗 Fluxo

+----------------------+ +------------------+ +-------------------+
| Feed Collectors | ---> | Database (SQL) | <--> | API REST (FastAPI) |
+----------------------+ +------------------+ +-------------------+
↑
|
+------------+-----------+
| Dashboard / Exportação |
+------------------------+