from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = "4.2.1"


def payment():
    return "Payment successful"


def product():
    return "Retail product"


def stock():
    return "In stock"


class RetailHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/":
            self.send_response(500)
            self.end_headers()
            self.wfile.write(
                f"Retail application - Version {VERSION}".encode()
            )

        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8081), RetailHandler)
    print(f"Retail application - Version {VERSION}")
    server.serve_forever()