#wybierz pracownika który zrobił najwięcej zadań
import requests
import json
from collections import defaultdict


r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    complitedTaskFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                complitedTaskFrequencyByUser[entry["userId"]] +=1
            except KeyError:
                complitedTaskFrequencyByUser[entry["userId"]] = 1
    return complitedTaskFrequencyByUser

def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]

def show_user_max_completedTask(complitedTaskFrequencyByUser):
    userIdMaxAmountOfComplitedTask = []
    maxAmountOfComplitedTask = max(complitedTaskFrequencyByUser.values())
    for userId, numberCompletedTask in complitedTaskFrequencyByUser.items():
        if numberCompletedTask == maxAmountOfComplitedTask:
            userIdMaxAmountOfComplitedTask.append(userId)
    return userIdMaxAmountOfComplitedTask


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    complitedTaskFrequencyByUser = count_task_frequency(tasks)
    userIdMaxAmountOfComplitedTask = show_user_max_completedTask(complitedTaskFrequencyByUser)
    print(f"Pracownikami roku są {userIdMaxAmountOfComplitedTask}")

#pobierz dane uzytkowników którzy wygrali
#1 sposób
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()
for user in users:
    if user["id"] in userIdMaxAmountOfComplitedTask:
        print(f"Wręczamy ciasteczko", (user["name"]))



