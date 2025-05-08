# Bürgergeld Chatbot

Ein einfacher KI-Chatbot, der automatisch Briefe vom Jobcenter analysiert und dem Benutzer hilft, passende Antworten zu erstellen.

## Anforderungen

- Python 3.10+
- Tesseract
- Poppler (für PDF → Bild)
- Pip-Bibliotheken: pytesseract, pdf2image, rich

## Schnellstart

1. `pip install -r requirements.txt`
2. `python app/main.py`

## Projektstruktur

- `app/main.py` – Einstiegspunkt
- `ocr_utils.py` – PDF → Text
- `analyzer.py` – Textanalyse
- `response_generator.py` – Antworterstellung