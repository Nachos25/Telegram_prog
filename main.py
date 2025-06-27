from tg_client.fetch_dialogs import fetch_recent_dialogs
from analysis.analyze_dialogs import analyze_dialogs
from report.generate_report import generate_report

if __name__ == "__main__":
    print("Добро пожаловать в анализатор Telegram-диалогов!")
    dialogs = fetch_recent_dialogs()
    analysis_results = analyze_dialogs(dialogs)
    generate_report(analysis_results) 