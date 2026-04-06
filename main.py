from environment import BatteryEnv
from models import Action

def run_baseline():
    env = BatteryEnv()
    state = env.reset()
    total_reward = 0  # <--- Yeh line check karo
    steps = 100

    print(f"--- Running Smart Baseline for {steps} steps ---")
    
    for i in range(steps):
        # Smart Logic
        if state.charge < 30 and state.is_charging:
            action_val = 2 
        elif state.temp > 48:
            action_val = 1
        else:
            action_val = 0
            
        action = Action(mode=action_val)
        state, reward, done, _ = env.step(action)
        total_reward += reward # <--- Reward yahan add ho raha hai
        
        if done: break

    # Final Score Calculation
    final_score = min(1.0, total_reward / 80.0) 
    print(f"Final Baseline Score: {final_score:.2f}")

if __name__ == "__main__":
    run_baseline()
    
    # Hugging Face ko zinda rakhne ke liye loop
    import time
    while True:
        time.sleep(10)