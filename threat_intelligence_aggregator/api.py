from fastapi import FastAPI
from typing import List

app = FastAPI(title="Threat Intelligence Feed Aggregator")


@app.get("/")
def read_root():
    return {"status": "running", "message": "Threat Intelligence Feed Aggregator"}

@app.get("/status")
def status():
    return {"status": "OK"}

@app.get("/feeds")
def list_feeds():
    return {
        "feeds": [
            "AbuseIPDB",
            "AlienVault OTX",
            "ThreatFox",
            "VirusTotal"
        ]
    }

@app.get("/lookup/{ioc}")
def lookup_ioc(ioc: str):
    # Aqui você implementaria a consulta real nos dados
    return {"ioc": ioc, "status": "Found", "details": "Example Data"}
