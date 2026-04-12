import os
import time
import http.server
import socketserver
import threading

# 1. SMART SERVER (Jo 'POST' error ko khatam karega)
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"status": "ok"}')
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Server is running!')

# Background mein server chalao
def start_server():
    with socketserver.TCPServer(("", 7860), MyHandler) as httpd:
        httpd.serve_forever()

threading.Thread(target=start_server, daemon=True).start()

# 2. TERA LOGIC (START/STEP/END)
def run():
    print("START")
    for _ in range(3):
        print("STEP")
        time.sleep(1)
    print("END")

if __name__ == "__main__":
    run()
    # Program ko zinda rakhne ke liye infinite loop
    while True:
        time.sleep(10)
