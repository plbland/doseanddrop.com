#!/usr/bin/env python3
"""
Simple HTTP server to test URL routing locally
This mimics how the production server will handle clean URLs

Usage: python3 test-server.py
Then visit: http://localhost:8000/privacy
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class RoutingHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Custom handler that routes clean URLs to .html files"""

    def do_GET(self):
        # Route mapping
        routes = {
            '/privacy': '/privacy.html',
            '/contact': '/contact.html',
        }

        # Check if the path matches a route
        if self.path in routes or self.path.rstrip('/') in routes:
            # Remove trailing slash if present
            clean_path = self.path.rstrip('/')
            # Map to actual file
            self.path = routes.get(clean_path, routes.get(self.path))

        # Serve the file
        return SimpleHTTPRequestHandler.do_GET(self)

def run_server(port=8000):
    """Start the test server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, RoutingHTTPRequestHandler)

    print(f"""
╔════════════════════════════════════════════════════╗
║  Dose & Drop Test Server                           ║
╠════════════════════════════════════════════════════╣
║  Server running at: http://localhost:{port}         ║
║                                                    ║
║  Test these URLs:                                  ║
║  • http://localhost:{port}/                        ║
║  • http://localhost:{port}/privacy                 ║
║  • http://localhost:{port}/contact                 ║
║                                                    ║
║  Press Ctrl+C to stop                              ║
╚════════════════════════════════════════════════════╝
    """)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        httpd.shutdown()

if __name__ == '__main__':
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_server()
