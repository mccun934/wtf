from http.server import BaseHTTPRequestHandler, HTTPServer

class Always500HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_error(500, "FOIGWTD")

    def do_POST(self):
        self.send_error(500, "FOIGWTD")

    def do_PUT(self):
        self.send_error(500, "FOIGWTD")

    # Add other methods (PUT, DELETE, etc.) if needed, following the same pattern

def run(server_class=HTTPServer, handler_class=Always500HTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

