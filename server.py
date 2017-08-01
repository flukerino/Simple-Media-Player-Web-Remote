from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import mimetypes
import os
import sys

import config
import media_control

WEB_ROOT = "./web-content"

playback_commands = {
    "play" : media_control.play,
    "pause" : media_control.pause,
    "stop" : media_control.stop,
    "previous_track" : media_control.previous_track,
    "next_track" : media_control.next_track,
}

files_whitelist = [
    "index.htm",
    "images/media-eject.png",
    "images/media-playback-pause.png",
    "images/media-playback-start.png",
    "images/media-playback-stop.png",
    "images/media-seek-backward.png",
    "images/media-seek-forward.png",
    "images/media-skip-backward.png",
    "images/media-skip-forward.png",
]

class RequestHandler(BaseHTTPRequestHandler):
    def _respond_status(self, status_code):
        self.send_response(status_code) 
        self.send_header('Content-Type', "text/html")
        self.end_headers()
        if status_code == 404:
            self.wfile.write("404 Not Found".encode("utf-8"))
        elif status_code == 500:
            self.wfile.write("500 Internal Server Error".encode("utf-8"))
            
    def do_GET(self):
        filename = self.path
        
        # Only valid QS are the single-valued ones defined in playback_commands not following any resource name
        if filename.startswith("/?"):
            cmd = filename[2:]
            if cmd not in playback_commands:
                self._respond_status(500)
                return
            else:
                print("-> \"{}\"".format(cmd))
                playback_commands[cmd]()
                self._respond_status(200)    # 204 (No Content) is better suited, but use 200 to be safe
                return
                
        if filename == "/":
            filename = "/index.htm"
        if not filename.startswith("/") or filename[1:] not in files_whitelist:
            self._respond_status(404)
            return
        
        # NOTE: if whitelist is removed, path traversal needs to be checked for here ("GET /../server.py" ...)
        filename = WEB_ROOT + filename
        if not os.path.exists(filename):
            self._respond_status(404)
            return
        
        # This was a valid request, respond with file
        self.send_response(200)
        mime = mimetypes.guess_type(filename)
        self.send_header('Content-Type', mime[0] if mime[0] else "application/octet-stream")
        if mime[1]:
            self.send_header('Content-Encoding', mime[1])
        self.end_headers()
        with open(filename,"rb") as f:
                self.wfile.write(f.read())


server_address = ("", config.SERVER_PORT)
httpd = HTTPServer(server_address, RequestHandler)

print("Starting server on port {}...".format(config.SERVER_PORT))
httpd.serve_forever()