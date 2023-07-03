from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        todos = ["Eat breakfast", "Go to work", "Work", "Go home", "Eat dinner", "Sleep"]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str(todos).encode())
        return