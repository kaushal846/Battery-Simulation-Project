import numpy as np
from models import Observation, Action

class BatteryEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.charge = 80.0
        self.temp = 25.0
        self.steps = 0
        return self.state()

    def state(self):
        return Observation(
            charge=max(0.0, float(self.charge)),
            temp=float(self.temp),
            load_demand=float(np.random.uniform(1.0, 5.0)),
            is_charging=(self.steps % 5 < 2) # Frequent charging windows
        )

    def step(self, action: Action):
        self.steps += 1
        
        # Physics
        if action.mode == 0: # Discharge
            self.charge -= 1.5 # Thoda kam decrease
            self.temp += 0.3
        elif action.mode == 2: # Charge
            self.charge += 4.0 # Faster charging
            self.temp += 0.6
        else: # Idle
            self.temp -= 0.4
            
        self.charge = np.clip(self.charge, 0, 100)
        self.temp = np.clip(self.temp, 20, 60)

        # --- HACKATHON REWARD LOGIC ---
        reward = 0.0
        
        # 1. Survival Reward (Har step zinda rehne ke 0.5 points)
        reward += 0.5 
        
        # 2. Health Bonus (Agar battery 30-90% ke beech hai)
        if 30 <= self.charge <= 90:
            reward += 0.3
            
        # 3. Safety Penalty (Agar overheat ho raha hai toh kaato)
        if self.temp > 50:
            reward -= 0.5
        
        # 4. Critical Failure
        done = self.steps >= 100 or self.charge <= 0
        if self.charge <= 0:
            reward -= 10.0 # Heavy penalty for dying

        return self.state(), reward, done, {}