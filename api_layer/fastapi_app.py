"""
fastapi_app.py

API layer exposing AWS Cost Optimization Engine.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from optimization_engine import (
    IdleResourceDetector,
    RightsizingAnalyzer,
    SavingsEstimator
)

app = FastAPI(
    title="AWS Cost Optimization Dashboard API",
    description="API for detecting idle resources, rightsizing opportunities, and savings estimation.",
    version="1.0"
)


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.get("/idle-resources")
def get_idle_resources():
    detector = IdleResourceDetector()
    df = detector.analyze()
    return JSONResponse(content=df.to_dict(orient="records"))


@app.get("/rightsizing")
def get_rightsizing():
    analyzer = RightsizingAnalyzer()
    df = analyzer.analyze()
    return JSONResponse(content=df.to_dict(orient="records"))


@app.get("/savings")
def get_savings():
    estimator = SavingsEstimator()
    df = estimator.estimate()
    return JSONResponse(content=df.to_dict(orient="records"))


@app.get("/full-report")
def get_full_report():
    detector = IdleResourceDetector()
    rightsizer = RightsizingAnalyzer()
    estimator = SavingsEstimator()

    return {
        "idle_recommendations": detector.analyze().to_dict(orient="records"),
        "rightsizing": rightsizer.analyze().to_dict(orient="records"),
        "savings": estimator.estimate().to_dict(orient="records"),
    }


@app.get("/summary")
def get_summary():
    """
    Lightweight summary for dashboard stat panels
    """
    detector = IdleResourceDetector()
    rightsizer = RightsizingAnalyzer()
    estimator = SavingsEstimator()

    idle_df = detector.analyze()
    right_df = rightsizer.analyze()
    savings_df = estimator.estimate()

    return {
        "idle_count": len(idle_df),
        "rightsizing_count": len(right_df),
        "estimated_total_savings": float(savings_df["estimated_savings"].sum())
        if "estimated_savings" in savings_df.columns else 0.0
    }

# ------------------------------------------------------------------
# ✅ GRAFANA-SPECIFIC ENDPOINTS (Flat JSON format for visualization)
# These DO NOT affect your main API — only used by Grafana dashboards.
# ------------------------------------------------------------------

@app.get("/grafana/idle")
def grafana_idle():
    detector = IdleResourceDetector()
    df = detector.analyze()
    return df.to_dict(orient="records")


@app.get("/grafana/rightsizing")
def grafana_rightsizing():
    analyzer = RightsizingAnalyzer()
    df = analyzer.analyze()
    return df.to_dict(orient="records")


@app.get("/grafana/savings")
def grafana_savings():
    estimator = SavingsEstimator()
    df = estimator.estimate()
    return df.to_dict(orient="records")
