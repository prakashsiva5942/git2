from sqlalchemy import Column,Integer,String,Float,Date,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class ProductionBatch(Base):
    __tablename__="production_batches"
    id=Column(Integer,primary_key=True,index=True)
    batch_code=Column(String,unique=True)
    date=Column(Date)
    shift=Column(String)
    created_by=Column(String)
    stages=relationship("Stagelog",back_populates="batch")

class ProcessStage(Base):
    __tablename__="process_stages"
    id=Column(Integer,primary_key=True)
    name=Column(String,unique=True)

class StageLog(Base):
   __tablename__="stage_logs"
   id=Column(Integer,primary_key=True,index=True) 
   production_batch_id=Column(Integer,ForeignKey("production_batches.id"))
   stage_id=Column(Integer,ForeignKey("process_stages.id"))
   input_material_batch=Column(String)
   input_quantity=Column(Float)
   output_quantity=Column(Float)
   machine_id=Column(String)
   operator_name=Column(String)
   start_time=Column(DateTime)
   end_time=Column(DateTime)
   remarks=Column(String)

   batch=relationship("ProductionBatch",back_populates="stages")
   stage=relationship("ProcessStage")