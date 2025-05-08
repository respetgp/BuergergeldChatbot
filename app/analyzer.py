def analyze_text(text):
    if "Mitwirkung" in text:
        return "fehlende Mitwirkungspflicht"
    elif "Einkommen" in text:
        return "unklare Angaben zum Einkommen"
    elif "Meldepflicht" in text:
        return "Verstoß gegen Meldepflicht"
    elif "Kontoauszug" in text:
        return "fehlende Kontoauszüge"
    else:
        return "Nicht erkannte Problematik"