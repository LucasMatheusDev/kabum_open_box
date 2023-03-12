import time
from datetime import datetime

import schedule as schedule


def search_schedule(task, hours: list):
    print("Agendando tarefas!")
    now = datetime.now()
    remaining_hours = []
    for hour in hours:
        next_hour = datetime.strptime("{} {}".format(now.strftime("%Y-%m-%d"), hour), "%Y-%m-%d %H:%M")
        if next_hour > now:
            remaining_hours.append(next_hour)
            schedule.every().day.at(hour).do(task)

    while True:
        if not remaining_hours:
            break
        next_run = min(remaining_hours)
        remaining_hours.remove(next_run)
        time_to_wait = (next_run - datetime.now()).total_seconds()
        print(f"Aguardando a próxima execução em {time_to_wait} segundos")
        time.sleep(time_to_wait)
        schedule.run_pending()
