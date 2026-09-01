#!/usr/bin/env python3
"""Push the aligned CV (``~/jobhunt/cv.md``) into a Google Docs copy of Mehdi's
"CV" Google Doc, leaving the original untouched.

Reusable for any iteration: edit ~/jobhunt/cv.md, re-run this, it makes a fresh
"CV - v2 Hermes" copy with the new content. Re-find the source doc ID if it
changes with:
    python <google-workspace>/scripts/google_api.py drive search "CV" --max 10
(look for mimeType 'application/vnd.google-apps.document', name "CV").
"""
import sys, re, json

SCRIPTS = "/root/.hermes/skills/productivity/google-workspace/scripts"
sys.path.insert(0, SCRIPTS)
from google_api import get_credentials, build_service

ORIG_ID = "1dsLagyGUB8dLLfp2cKo6_3FXvVN47H2Hi9HzMFLL_Ok"

creds = get_credentials()
docs = build_service("docs", "v1")

def doc_text(d):
    parts = []
    for e in d.get("body", {}).get("content", []):
        p = e.get("paragraph", {})
        for pe in p.get("elements", []):
            tr = pe.get("textRun", {})
            if tr.get("content"):
                parts.append(tr["content"])
    return "".join(parts)

orig = docs.documents().get(documentId=ORIG_ID).execute()
print("=== ORIGINAL 'CV' DOC (first 400 chars) ===")
print(doc_text(orig)[:400])
print("=== END ORIGINAL ===")

drive = build_service("drive", "v3")
cp = drive.files().copy(fileId=ORIG_ID, body={"name": "CV - v2 Hermes"}).execute()
new_id = cp["id"]

md = open("/root/jobhunt/cv.md").read()
lines = []
for line in md.split("\n"):
    line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)   # strip bold
    line = re.sub(r"^#+\s*", "", line)              # strip header markers
    lines.append(line)
text = "\n".join(lines).strip() + "\n"

newdoc = docs.documents().get(documentId=new_id).execute()
end = newdoc["body"]["content"][-1]["endIndex"]
reqs = [
    {"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end - 1}}},
    {"insertText": {"location": {"index": 1}, "text": text}},
]
docs.documents().batchUpdate(documentId=new_id, body={"requests": reqs}).execute()

print("=== DONE ===")
print("https://docs.google.com/document/d/" + new_id + "/edit")
print("ID:", new_id)
