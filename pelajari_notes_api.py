#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pelajari Notes & Attachments API Daemon
Port: 8658
Provides timeline learning notes storage and file/photo upload for Pelajari Masterclass OS.
"""

import os
import sys
import json
import uuid
import re
import base64
import mimetypes
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

PORT = 8658

# Base directory detection
if os.path.exists("/var/www/pelajari"):
    BASE_DIR = "/var/www/pelajari"
elif os.path.exists("/root/pelajari"):
    BASE_DIR = "/root/pelajari"
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")

def ensure_storage():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

ensure_storage()

def load_notes():
    ensure_storage()
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[API] Error loading notes: {e}", file=sys.stderr)
        return []

def save_notes(notes):
    ensure_storage()
    tmp_file = NOTES_FILE + f".tmp_{os.getpid()}_{uuid.uuid4().hex[:6]}"
    try:
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
        os.replace(tmp_file, NOTES_FILE)
        return True
    except Exception as e:
        print(f"[API] Error saving notes: {e}", file=sys.stderr)
        if os.path.exists(tmp_file):
            try:
                os.remove(tmp_file)
            except Exception:
                pass
        return False

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".bmp", ".avif"}

def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    return "image" if ext in IMAGE_EXTENSIONS else "file"

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

class NotesAPIHandler(BaseHTTPRequestHandler):
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")

    def send_json(self, status_code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_cors_headers()
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors_headers()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        url_path = self.path.split("?")[0].rstrip("/")
        # Normalize url: strip /api if present
        clean_path = url_path
        if clean_path.startswith("/api"):
            clean_path = clean_path[4:]
        if clean_path.startswith("/pelajari/api"):
            clean_path = clean_path[13:]
        clean_path = clean_path.rstrip("/")

        if clean_path in ("", "/health"):
            notes = load_notes()
            return self.send_json(200, {
                "ok": True,
                "status": "online",
                "service": "Pelajari Notes & Attachments API",
                "total_notes": len(notes)
            })

        if clean_path == "/notes":
            # Support query string filtering (?course=...&module=...)
            query = {}
            if "?" in self.path:
                qs = self.path.split("?", 1)[1]
                for part in qs.split("&"):
                    if "=" in part:
                        k, v = part.split("=", 1)
                        query[k] = v

            notes = load_notes()
            # Sort newest first
            notes.sort(key=lambda x: x.get("created_at", ""), reverse=True)

            if "course" in query and query["course"]:
                notes = [n for n in notes if n.get("course_id") == query["course"]]
            if "module" in query and query["module"]:
                notes = [n for n in notes if n.get("module_id") == query["module"]]

            return self.send_json(200, {
                "ok": True,
                "count": len(notes),
                "notes": notes
            })

        return self.send_json(404, {"ok": False, "error": "Not Found"})

    def do_POST(self):
        url_path = self.path.split("?")[0].rstrip("/")
        clean_path = url_path
        if clean_path.startswith("/api"):
            clean_path = clean_path[4:]
        if clean_path.startswith("/pelajari/api"):
            clean_path = clean_path[13:]
        clean_path = clean_path.rstrip("/")

        content_length = int(self.headers.get("Content-Length", 0))
        if content_length <= 0:
            return self.send_json(400, {"ok": False, "error": "Empty body"})

        raw_body = self.rfile.read(content_length)

        # -------------------------------------------------------------
        # Endpoint: POST /upload (Upload photo / file via JSON Base64 or Multipart)
        # -------------------------------------------------------------
        if clean_path == "/upload":
            content_type = self.headers.get("Content-Type", "")
            
            # Handle JSON Base64 upload
            if "application/json" in content_type:
                try:
                    payload = json.loads(raw_body.decode("utf-8"))
                except Exception as e:
                    return self.send_json(400, {"ok": False, "error": f"Invalid JSON: {e}"})

                filename = payload.get("filename", "file.bin")
                b64data = payload.get("data", "")
                if "," in b64data:
                    # Strip data:image/png;base64,... header
                    b64data = b64data.split(",", 1)[1]

                try:
                    file_bytes = base64.b64decode(b64data)
                except Exception as e:
                    return self.send_json(400, {"ok": False, "error": f"Invalid Base64: {e}"})

                if len(file_bytes) > 25 * 1024 * 1024:
                    return self.send_json(400, {"ok": False, "error": "Ukuran file melebihi batas 25MB"})

                # Clean filename
                ext = os.path.splitext(filename)[1].lower()
                safe_stem = re.sub(r"[^a-zA-Z0-9_\-]", "_", os.path.splitext(filename)[0])[:32]
                safe_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}_{safe_stem}{ext}"
                target_path = os.path.join(UPLOADS_DIR, safe_name)

                with open(target_path, "wb") as f:
                    f.write(file_bytes)

                file_type = get_file_type(safe_name)
                mime_type = mimetypes.guess_type(safe_name)[0] or "application/octet-stream"

                return self.send_json(200, {
                    "ok": True,
                    "url": f"/pelajari/uploads/{safe_name}",
                    "filename": safe_name,
                    "original_name": filename,
                    "size": len(file_bytes),
                    "type": file_type,
                    "mime": mime_type
                })

            # Handle multipart/form-data upload
            elif "multipart/form-data" in content_type:
                try:
                    boundary = content_type.split("boundary=")[1].encode("utf-8")
                except Exception:
                    return self.send_json(400, {"ok": False, "error": "Invalid multipart boundary"})

                parts = raw_body.split(b"--" + boundary)
                saved_file = None

                for part in parts:
                    if b'filename="' in part:
                        header_part, body_part = part.split(b"\r\n\r\n", 1)
                        header_str = header_part.decode("latin1")
                        m = re.search(r'filename="([^"]+)"', header_str)
                        if m:
                            filename = os.path.basename(m.group(1))
                            # Strip trailing \r\n
                            if body_part.endswith(b"\r\n"):
                                body_part = body_part[:-2]

                            if len(body_part) > 25 * 1024 * 1024:
                                return self.send_json(400, {"ok": False, "error": "Ukuran file melebihi batas 25MB"})

                            ext = os.path.splitext(filename)[1].lower()
                            safe_stem = re.sub(r"[^a-zA-Z0-9_\-]", "_", os.path.splitext(filename)[0])[:32]
                            safe_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}_{safe_stem}{ext}"
                            target_path = os.path.join(UPLOADS_DIR, safe_name)

                            with open(target_path, "wb") as f:
                                f.write(body_part)

                            file_type = get_file_type(safe_name)
                            mime_type = mimetypes.guess_type(safe_name)[0] or "application/octet-stream"
                            saved_file = {
                                "ok": True,
                                "url": f"/pelajari/uploads/{safe_name}",
                                "filename": safe_name,
                                "original_name": filename,
                                "size": len(body_part),
                                "type": file_type,
                                "mime": mime_type
                            }
                            break

                if saved_file:
                    return self.send_json(200, saved_file)
                return self.send_json(400, {"ok": False, "error": "No file found in multipart upload"})

            else:
                return self.send_json(400, {"ok": False, "error": "Unsupported Content-Type. Use JSON base64 or multipart/form-data"})

        # -------------------------------------------------------------
        # Endpoint: POST /notes (Create learning note)
        # -------------------------------------------------------------
        if clean_path == "/notes":
            try:
                payload = json.loads(raw_body.decode("utf-8"))
            except Exception as e:
                return self.send_json(400, {"ok": False, "error": f"Invalid JSON: {e}"})

            content = (payload.get("content") or "").strip()
            attachments = payload.get("attachments") or []

            if not content and not attachments:
                return self.send_json(400, {"ok": False, "error": "Catatan tidak boleh kosong"})

            now_iso = datetime.now(timezone.utc).isoformat()
            new_note = {
                "id": "note_" + uuid.uuid4().hex[:12],
                "created_at": now_iso,
                "updated_at": now_iso,
                "course_id": payload.get("course_id", "general"),
                "course_title": payload.get("course_title", "General"),
                "module_id": payload.get("module_id", "overview"),
                "module_title": payload.get("module_title", "Overview"),
                "content": content,
                "attachments": attachments
            }

            notes = load_notes()
            notes.insert(0, new_note)
            if save_notes(notes):
                return self.send_json(201, {"ok": True, "note": new_note})
            else:
                return self.send_json(500, {"ok": False, "error": "Gagal menyimpan catatan ke disk"})

        return self.send_json(404, {"ok": False, "error": "Not Found"})

    def do_DELETE(self):
        url_path = self.path.split("?")[0].rstrip("/")
        clean_path = url_path
        if clean_path.startswith("/api"):
            clean_path = clean_path[4:]
        if clean_path.startswith("/pelajari/api"):
            clean_path = clean_path[13:]
        clean_path = clean_path.rstrip("/")

        # Format: DELETE /notes/<id>
        m = re.match(r"^/notes/([^/]+)$", clean_path)
        if m:
            note_id = m.group(1)
            notes = load_notes()
            initial_count = len(notes)
            filtered = [n for n in notes if n.get("id") != note_id]

            if len(filtered) == initial_count:
                return self.send_json(404, {"ok": False, "error": "Note not found"})

            if save_notes(filtered):
                return self.send_json(200, {"ok": True, "deleted_id": note_id})
            else:
                return self.send_json(500, {"ok": False, "error": "Gagal menghapus catatan"})

        return self.send_json(404, {"ok": False, "error": "Not Found"})

def run():
    server_address = ("0.0.0.0", PORT)
    httpd = ThreadedHTTPServer(server_address, NotesAPIHandler)
    print(f"[API] Pelajari Notes & Attachments Server running on port {PORT} (Base: {BASE_DIR})")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[API] Shutting down server...")
        httpd.server_close()

if __name__ == "__main__":
    run()
