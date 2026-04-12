import os
import time
import http.server
import socketserver
import threading
from environment import BatteryEnv
from models import Action

# --- YE HAI DUMMY SERVER (Hugging Face ko 'Running' rakhne ke liye) ---
def start_dummy_server():
    handler = http.server.SimpleHTTPRequestHandler
    # Port 7860 Hugging Face ka default port hai
    with socketserver.TCPServer(("", 7860), handler) as httpd:
        httpd.serve_forever()

# Simulation shuru hone se pehle isey background mein chala do
threading.Thread(target=start_dummy_server, daemon=True).start()

def run_simulation():
    env = BatteryEnv()
    state = env.reset()
    done = False
    
    # --- UNKA FORMAT ---
    print("START")
    
    while not done:
        action = Action(mode=0)
        next_state, reward, done, info = env.step(action)
        print("STEP")
        
    print("END")

if __name__ == "__main__":
    run_simulation()
    
    # Loop taaki program turant band na ho
    while True:
        time.sleep(30)
