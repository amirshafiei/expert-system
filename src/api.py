from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from rule import Rule
from working_memory import WorkingMemory
from engine import InferenceEngine

app = FastAPI(title="Expert System API", version="0.1.0")

# -------------------------------
# مدل داده‌ای برای درخواست
# -------------------------------
class DiagnoseRequest(BaseModel):
    symptoms: List[str]                    # علائم ورودی
    rules: Optional[List[Rule]] = None     # قوانین اختیاری

# -------------------------------
# نمونه قوانین پیش‌فرض
# -------------------------------
DEFAULT_RULES = [
    Rule(id="cold", antecedents=["سرفه", "گلودرد"], consequent="احتمال سرماخوردگی", salience=10),
    Rule(id="flu", antecedents=["تب بالا", "سردرد", "بدن درد"], consequent="احتمال آنفولانزا", salience=10),
    Rule(id="allergy", antecedents=["عطسه", "آبریزش بینی"], consequent="احتمال آلرژی", salience=5),
]

# -------------------------------
# ایجاد یک Engine نمونه برای endpoint /rules
# -------------------------------
default_wm = WorkingMemory()
engine = InferenceEngine(DEFAULT_RULES, default_wm)

# -------------------------------
# مسیر تشخیص
# -------------------------------
@app.post("/diagnose")
def diagnose(req: DiagnoseRequest):
    # بارگذاری قوانین
    rules = req.rules or DEFAULT_RULES

    # ایجاد حافظه کاری با علائم ورودی
    wm = WorkingMemory(req.symptoms)

    # اجرای موتور استنتاج
    engine = InferenceEngine(rules, wm)
    conclusions = engine.forward_chain()
    explanation = engine.explain()

    return {
        "input_symptoms": req.symptoms,
        "conclusions": conclusions or ["تشخیص داده نشد"],
        "explanation": explanation,
    }

# -------------------------------
# مسیر تست قوانین پیش‌فرض
# -------------------------------
@app.get("/rules")
def get_rules():
    return {
        "rules": [
            {
                "id": rule.id,
                "if": rule.antecedents,
                "then": rule.consequent,
                "salience": rule.salience,
            }
            for rule in DEFAULT_RULES
        ]
    }