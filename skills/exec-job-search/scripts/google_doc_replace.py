#!/usr/bin/env python3
"""Replace a Google Doc's content with a local Markdown file (plain text).

Useful for publishing an aligned CV/doc to Google Drive for user review without
touching the original. Optionally copies the source doc first so the original
stays intact.

Requires the google-workspace skill's OAuth token (~/.hermes/google_token.json)
and its scripts dir on sys.path.

Usage:
  python google_doc_replace.py --doc-id ID --md file.md                    # replace in place
  python google_doc_replace.py --doc-id ID --md file.md --copy "CV - v2"   # copy then replace
"""
import sys, re, argparse

SCRIPTS = "/root/.hermes/skills/productivity/google-workspace/scripts"
sys.path.insert(0, SCRIPTS)
from google_api import get_credentials, build_service


def md_to_plain(path):
    lines = []
    with open(path) as f:
        for line in f.read().split("\n"):
            line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)   # strip bold
            line = re.sub(r"^#+\s*", "", line)              # strip header markers
            lines.append(line)
    return "\n".join(lines).strip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc-id", required=True, help="source Google Doc ID")
    ap.add_argument("--md", required=True, help="local markdown file to insert")
    ap.add_argument("--copy", help="copy first, using this new name")
    args = ap.parse_args()

    creds = get_credentials()
    target = args.doc_id

    if args.copy:
        drive = build_service("drive", "v3")
        cp = drive.files().copy(fileId=args.doc_id, body={"name": args.copy}).execute()
        target = cp["id"]
        print("Copied to:", target)

    text = md_to_plain(args.md)
    docs = build_service("docs", "v1")
    doc = docs.documents().get(documentId=target).execute()
    end = doc["body"]["content"][-1]["endIndex"]
    reqs = [
        {"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end - 1}}},
        {"insertText": {"location": {"index": 1}, "text": text}},
    ]
    docs.documents().batchUpdate(documentId=target, body={"requests": reqs}).execute()
    print("Updated:", target)
    print("https://docs.google.com/document/d/" + target + "/edit")


if __name__ == "__main__":
    main()
