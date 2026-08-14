import sys
import asyncio


from evaluation import token_level_eval
from fastapi import FastAPI, HTTPException
from parsers.factory import get_parser_for_url
from models import (
    ParseRequest, ParseResponse,
    DomainsResponse,
    GoldStandardResponse,
    GoldStandardUrlsResponse,
    EvaluateRequest, EvaluateResponse, TokenLevelEval,
    EvaluateJudgeResponse,
    StatusResponse,
    DbStatsResponse,
    DbSchemaResponse,
    FullGsEvalResponse
)
from config import DOMAINS

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Il backend funziona!"}


# --- GET /domains ---
@app.get("/domains", response_model=DomainsResponse)
def get_domains():
    return DomainsResponse(domains=DOMAINS)


# --- GET /status ---
@app.get("/status")
def get_status():
    return {
        "backend": "ok",
        "database": "error",   # placeholder, lo colleghiamo davvero al Punto 6
        "ollama": "error"      # placeholder, lo colleghiamo davvero al Punto 7
    }


# --- POST /parse ---
@app.post("/parse", response_model=ParseResponse)
async def parse_url(request: ParseRequest):
    parser = get_parser_for_url(request.url)

    if parser is None:
        raise HTTPException(status_code=400, detail="Dominio non supportato")

    try:
        result = await parser.parse(request.url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"URL irraggiungibile: {str(e)}")

    return ParseResponse(**result)

# --- GET /gold_standard ---
@app.get("/gold_standard", response_model=GoldStandardResponse)
def get_gold_standard(url: str):
    # TODO: qui andrà la vera lettura dal database (Punto 6)
    return GoldStandardResponse(
        url=url,
        domain="placeholder.it",
        title="Titolo di prova",
        html_text="<html>...</html>",
        gold_text="Testo gold di prova"
    )


# --- GET /gold_standard_urls ---
@app.get("/gold_standard_urls", response_model=GoldStandardUrlsResponse)
def get_gold_standard_urls(domain: str):
    if domain not in DOMAINS:
        raise HTTPException(status_code=400, detail="Dominio non supportato")
    # TODO: qui andrà la vera lettura dal database (Punto 6)
    return GoldStandardUrlsResponse(gold_standard_urls=[])


# --- POST /evaluate ---
@app.post("/evaluate", response_model=EvaluateResponse)
def evaluate(request: EvaluateRequest):
    # TODO: qui andrà la vera implementazione token_level_eval (Punto 7)
    fake_metrics = TokenLevelEval(precision=0.0, recall=0.0, f1=0.0)
    return EvaluateResponse(token_level_eval=fake_metrics)


# --- POST /evaluate_judge ---
@app.post("/evaluate_judge", response_model=EvaluateJudgeResponse)
def evaluate_judge(request: EvaluateRequest):
    # TODO: qui andrà la vera chiamata a Ollama (Punto 7)
    return EvaluateJudgeResponse(
        model_name="placeholder-model",
        judge_score=1,
        judge_feedback="Valutazione di prova"
    )


# --- POST /add_web_resource ---
@app.post("/add_web_resource", response_model=StatusResponse)
def add_web_resource(url: str, html_text: str):
    # TODO: qui andrà il vero salvataggio nel database (Punto 6)
    return StatusResponse(status="ok")


# --- POST /add_gold_standard ---
@app.post("/add_gold_standard", response_model=StatusResponse)
def add_gold_standard(url: str, gold_text: str):
    # TODO: qui andrà il vero salvataggio nel database (Punto 6)
    return StatusResponse(status="ok")


# --- DELETE /web_resource ---
@app.delete("/web_resource", response_model=StatusResponse)
def delete_web_resource(url: str):
    # TODO: qui andrà la vera cancellazione dal database (Punto 6)
    return StatusResponse(status="ok")


# --- DELETE /gold_standard ---
@app.delete("/gold_standard", response_model=StatusResponse)
def delete_gold_standard(url: str):
    # TODO: qui andrà la vera cancellazione dal database (Punto 6)
    return StatusResponse(status="ok")


# --- GET /full_gs_eval ---
@app.get("/full_gs_eval", response_model=FullGsEvalResponse)
def full_gs_eval(domain: str):
    if domain not in DOMAINS:
        raise HTTPException(status_code=400, detail="Dominio non supportato")
    # TODO: qui andrà la vera aggregazione delle valutazioni (Punto 6-7)
    fake_metrics = TokenLevelEval(precision=0.0, recall=0.0, f1=0.0)
    return FullGsEvalResponse(token_level_eval=fake_metrics, judge_score=0.0)


# --- GET /db_stats ---
@app.get("/db_stats", response_model=DbStatsResponse)
def db_stats():
    # TODO: qui andranno le vere statistiche dal database (Punto 6)
    return DbStatsResponse(
        web_resources={},
        gold_standard={},
        avg_eval={},
        avg_eval_judge={}
    )


# --- GET /db_schema ---
@app.get("/db_schema", response_model=DbSchemaResponse)
def db_schema():
    # TODO: qui andrà lo schema vero del database (Punto 6)
    return DbSchemaResponse(
        web_resources={
            "url": "varchar(2048), PK",
            "domain": "varchar(255)",
            "title": "varchar(2048)",
            "html_text": "longtext",
            "created_at": "datetime"
        },
        gold_standard={
            "url": "varchar(2048), PK, FK(web_resources.url)",
            "gold_text": "longtext",
            "created_at": "datetime"
        }
    )