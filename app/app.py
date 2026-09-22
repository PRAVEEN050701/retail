from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = "4.2.1"


def payment():
    return "Payment successful"


def product():
    return "Retail product"


def stock():
    return "In stock"


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"healthy")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                f"Retail application - Version {VERSION}".encode()
            )

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8081), Handler)
    server.serve_forever()