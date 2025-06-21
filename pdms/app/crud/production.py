from sqlalchemy.orm import Session
from app.models.production import ProductionBatch, StageLog, ProcessStage
from app.schemas.production import ProductionBatchCreate, StageLogCreate

def create_batch(db:Session,data:ProductionBatchCreate):
    batch=ProductionBatch(**data.dict())
    db.add(batch)
    db.commit()
    db.refresh(batch)
    return batch

def log_stage(db: Session, data: StageLogCreate):
    stage_log = StageLog(**data.dict())
    db.add(stage_log)
    db.commit()
    db.refresh(stage_log)
    return stage_log

def get_batch_flow(db:Session,batch_code:str):
   return db.query(StageLog).join(ProductionBatch).filter(ProductionBatch.batch_code == batch_code).all()