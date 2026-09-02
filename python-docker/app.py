# server.py

from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the request handler class
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    # Define the response to GET requests
    def do_GET(self):
        # Set response status code
        self.send_response(200)
        # Set headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the response body
        self.wfile.write(b"<h1>Hello, World!</h1>")

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    # Specify server address
    server_address = ('', port)
    # Create and run the server
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    # Run the server
    run()
