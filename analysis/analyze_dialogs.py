import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# AI-анализ диалогов

def analyze_dialogs(dialogs):
    results = []
    for dialog in dialogs:
        messages = dialog['messages']
        text = '\n'.join([
            f"{m.sender_id}: {m.text}" for m in messages if m.text
        ])
        prompt = (
            "Проанализируй переписку между менеджером и клиентом.\n"
            "1. Есть ли обещания менеджера, которые не были выполнены до конца дня?\n"
            "2. Есть ли негатив, ошибки, недовольство клиента или низкая инициативность менеджера?\n"
            "3. Выдели метрики: количество ответов менеджера, среднее время ответа, "
            "количество пропущенных сообщений, количество инициативных сообщений менеджера.\n\n"
            f"Переписка:\n{text}\n\n"
            "Ответь в формате JSON с ключами: 'unfulfilled_promises', 'negativity', 'metrics', 'summary'."
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        ai_result = response.choices[0].message['content']
        results.append({
            'dialog': dialog,
            'ai_result': ai_result
        })
    return results 