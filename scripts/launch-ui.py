#!/usr/bin/env python3
"""
AI PM Sidekick — PM Command Center Local Web UI Launcher
Launches a lightweight local HTTP web server serving the Google Stitch-designed PM Command Center GUI.

Usage:
  python3 scripts/launch-ui.py [--port 3000] [--open]
"""

import os
import sys
import argparse
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.resolve()
MOCKUP_FILE = ROOT_DIR / "mockups" / "pm-command-center.html"

class PMCommandCenterHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Default root path to pm-command-center.html
        clean_path = path.split('?')[0].split('#')[0]
        if clean_path in ('/', '/index.html', '/gui', '/dashboard'):
            return str(MOCKUP_FILE)
        return super().translate_path(path)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server(host="127.0.0.1", port=3000, open_browser=False):
    os.chdir(ROOT_DIR)
    server_address = (host, port)
    httpd = HTTPServer(server_address, PMCommandCenterHandler)
    url = f"http://{host}:{port}"

    print(f"\n=======================================================")
    print(f"🚀 AI PM Sidekick — PM Command Center UI")
    print(f"=======================================================")
    print(f"  • Interface:      Google Stitch Atelier Workspace")
    print(f"  • Local URL:      {url}")
    print(f"  • Security:       100% Localhost (Zero Cloud Leakage)")
    print(f"  • Status:         Active Daemon Listening")
    print(f"=======================================================\n")
    print("Press Ctrl+C to stop the server.\n")

    if open_browser:
        webbrowser.open(url)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down PM Command Center server. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch AI PM Sidekick Web GUI")
    parser.add_argument("--host", default="127.0.0.1", help="Host address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=3000, help="Port to listen on (default: 3000)")
    parser.add_argument("--open", action="store_true", help="Automatically open browser")
    args = parser.parse_args()

    run_server(host=args.host, port=args.port, open_browser=args.open)
