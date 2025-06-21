from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.production import ProductionBatchCreate, StageLogCreate,StageLogOut,ProductionBatchOut
from app.crud import production
from app.db.database import get_db
from typing import List

router =APIRouter(prefix="/production",tags=["Production"])



@router.post("/batch",response_model=ProductionBatchOut,status_code=201,summary="Create a production batch")
def create_production_batch(data:ProductionBatchCreate,db:Session=Depends(get_db)):
    return production.create_batch(db,data)
@router.get("/batch/",response_model=List[ProductionBatchOut])
def list_batches(db:Session=Depends(get_db)):
    return production.get_all_batches(db)
@router.post("/stage-log",response_model=StageLogOut, status_code=201,summary="Log a process stage entry")
def log_stage_entry(data:StageLogCreate,db:Session=Depends(get_db)):
    return production.create_stage_log(db,data)
@router.get("/batch/{batch_code}",response_model=List[StageLogOut],summary="View full batch production flow")
def get_full_batch_log(batch_code:str,db:Session=Depends(get_db)):
    return production.get_batch_flow(db,batch_code)
@router.put("/stage-log/{id}",response_model=StageLogOut)
def update_stage(id: int,data: StageLogCreate,db: Session = Depends(get_db)):
    return production.update_stage_log(db, id, data)