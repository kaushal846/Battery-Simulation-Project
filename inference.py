import os
import time
from environment import BatteryEnv
from models import Action

def run_simulation():
    # 1. Environment load karo
    env = BatteryEnv()
    state = env.reset()
    done = False
    
    # 2. UNKA ZAROORI FORMAT: Sabse pehle START print hona chahiye
    print("START")
    
    while not done:
        # 3. Yahan model action leta hai (abhi baseline mode 0 hai)
        action = Action(mode=0)
        next_state, reward, done, info = env.step(action)
        
        # 4. UNKA ZAROORI FORMAT: Har step par STEP print hona chahiye
        print("STEP")
        
    # 5. UNKA ZAROORI FORMAT: Khatam hone par END print hona chahiye
    print("END")

if __name__ == "__main__":
    run_simulation()
    
    # Hugging Face Space ko "Running" rakhne ke liye loop
    while True:
        time.sleep(30)
