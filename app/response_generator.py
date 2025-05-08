def generate_client_response(problem):
    return f"Джобцентр сообщает, что у вас проблема: {problem}."

def generate_jobcenter_letter(problem):
    return f"""Sehr geehrte Damen und Herren,

ich habe Ihr Schreiben erhalten. Laut Ihrem Bescheid gibt es folgendes Problem: {problem}.

Ich bitte Sie um eine Klärung und stehe für Rückfragen gerne zur Verfügung.

Mit freundlichen Grüßen,
[Имя клиента]
"""