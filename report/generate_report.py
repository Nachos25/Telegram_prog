import pandas as pd
import matplotlib.pyplot as plt
import json


def generate_report(analysis_results):
    print('Формирую отчёт...')
    rows = []
    for res in analysis_results:
        dialog = res['dialog']
        ai = json.loads(res['ai_result'])
        rows.append({
            'Чат': dialog['name'],
            'Невыполненные обещания': ai.get('unfulfilled_promises'),
            'Негатив/ошибки': ai.get('negativity'),
            'Метрики': ai.get('metrics'),
            'Кратко': ai.get('summary')
        })
    df = pd.DataFrame(rows)
    print(df)
    # Визуализация: количество негативных чатов
    neg_count = df['Негатив/ошибки'].apply(
        lambda x: bool(x) and x != '[]'
    ).sum()
    plt.bar(
        ['Негативные чаты', 'Всего чатов'],
        [neg_count, len(df)]
    )
    plt.title('Статистика по чатам')
    plt.show() 