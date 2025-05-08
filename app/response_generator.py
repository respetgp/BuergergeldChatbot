from app.openai_utils import chat_with_model

def summarize_letter(text: str) -> str:
    prompt = (
        f"Это текст письма от Jobcenter:\n\n"
        f"{text}\n\n"
        "На русском языке: Опишите суть этого письма и укажите, что от клиента требуется."
    )
    messages = [{"role": "user", "content": prompt}]
    return chat_with_model(messages)

def generate_jobcenter_letter(reply_text: str) -> str:
    prompt = (
        f"Клиент хочет ответить так:\n{reply_text}\n\n"
        "Составьте вежливое официальное письмо на немецком языке в Jobcenter."
    )
    messages = [{"role": "user", "content": prompt}]
    return chat_with_model(messages)

def explain_problem(problem):
    prompt = (
        f"На русском языке: Джобцентр сообщает, что у клиента проблема: {problem}. "
        f"Объясни человеку, в чём суть и как её можно решить."
    )
    messages = [{"role": "user", "content": prompt}]
    return chat_with_model(messages)

def generate_jobcenter_letter(problem):
    prompt = (
        f"Составь вежливое официальное письмо на немецком языке в Jobcenter с просьбой разъяснить ситуацию. "
        f"Проблема: {problem}. Используй официальный стиль."
    )
    messages = [{"role": "user", "content": prompt}]
    return chat_with_model(messages)