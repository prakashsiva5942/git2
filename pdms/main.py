
from fastapi import FastAPI
from app.api import production_routes
from app.db.database import Base,engine
from app.models.production import ProductionBatch,StageLog,ProcessStage
app=FastAPI(
    title="PDMS-Production Entry",
    version="1.0.0",
    description="Production Process Logging API"
    )
Base.metadata.create_all(bind=engine)
app.include_router(production_routes.router)