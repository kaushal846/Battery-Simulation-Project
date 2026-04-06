from pydantic import BaseModel
from typing import Dict

class Observation(BaseModel):
    charge: float      # 0.0 to 100.0
    temp: float        # Celsius
    load_demand: float # Current power needed
    is_charging: bool  # Is it plugged in?

class Action(BaseModel):
    # 0: Discharge, 1: Idle, 2: Charge
    mode: int