from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime, date

class ProductionBatchCreate(BaseModel):
    batch_code:str
    date:date
    shift:str
    created__by:str

class StageLogCreate(BaseModel):
    production_batch_id:int
    stage_id:int
    input_material_batch:str
    input_quantity:float
    output_quantity:float
    machine_id:str
    operator_name:str
    start_time:datetime
    end_time:datetime
    remarks:Optional[str]

class ProductionBatchOut(BaseModel):
    id:int
    batch_code:str
    date:date
    shift:str
    created_by:str
    class Config:
        from_attributes=True
class StageLogOut(BaseModel):
    id:int
    production_batch_id:int
    stage_id:int
    input_material_batch:str
    input_quantity:float
    output_quantity:float
    machine_id:str
    operator_name:str
    start_time:datetime
    end_time:datetime
    remarks:Optional[str]=None
    class Config:
        from_attributes=True

    @field_validator("end_time")
    def check_time(cls,end,values):
        if 'start_time' in values and end<=values["start_time"]:
            raise ValueError("End time must be after start time")
        return end
    
    @field_validator("output_quantity")
    def output_not_greater(cls,out,values):
        if 'input_quantity'in values and out>values['input_quantity']:
            raise ValueError("Output cannot exceed input")
        return out
    