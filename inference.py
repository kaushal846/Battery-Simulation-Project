import http.server
import socketserver
import threading

# --- SMART DUMMY SERVER (Har request ko OK bolega) ---
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"status": "ok"}')

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Server is running!')

def start_smart_server():
    handler = MyHandler
    # Port 7860 Hugging Face ke liye
    with socketserver.TCPServer(("", 7860), handler) as httpd:
        httpd.serve_forever()

# Background mein chalao
threading.Thread(target=start_smart_server, daemon=True).start()
