from pydantic import BaseModel
from typing import Optional, List, Dict


# --- Modelli per /parse ---
class ParseRequest(BaseModel):
    url: str
    local: Optional[bool] = False

class ParseResponse(BaseModel):
    url: str
    domain: str
    title: str
    html_text: str
    parsed_text: str


# --- Modelli per /domains ---
class DomainsResponse(BaseModel):
    domains: List[str]


# --- Modelli per /gold_standard ---
class GoldStandardResponse(BaseModel):
    url: str
    domain: str
    title: str
    html_text: str
    gold_text: str


# --- Modelli per /gold_standard_urls ---
class GoldStandardUrlsResponse(BaseModel):
    gold_standard_urls: List[str]


# --- Modelli per /evaluate ---
class EvaluateRequest(BaseModel):
    parsed_text: str
    gold_text: str

class TokenLevelEval(BaseModel):
    precision: float
    recall: float
    f1: float

class EvaluateResponse(BaseModel):
    token_level_eval: TokenLevelEval


# --- Modelli per /evaluate_judge ---
class EvaluateJudgeResponse(BaseModel):
    model_name: str
    judge_score: int
    judge_feedback: str


# --- Modelli generici per status/ok ---
class StatusResponse(BaseModel):
    status: str



# --- Modelli per /db_stats ---
class DbStatsResponse(BaseModel):
    web_resources: Dict[str, int]
    gold_standard: Dict[str, int]
    avg_eval: Dict[str, dict]
    avg_eval_judge: Dict[str, dict]


# --- Modelli per /db_schema ---
class DbSchemaResponse(BaseModel):
    web_resources: Dict[str, str]
    gold_standard: Dict[str, str]


# --- Modelli per /full_gs_eval ---
class FullGsEvalResponse(BaseModel):
    token_level_eval: TokenLevelEval
    judge_score: float