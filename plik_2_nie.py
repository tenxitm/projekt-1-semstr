import projekt

task_bar = ["0/3"]
print(task_bar)

projekt.task_1()

print("-" * 50)

task_bar.remove("0/3")
task_bar.append("1/3")
print(f'TASK BAR{task_bar}')


print("-" * 50)


projekt.voting()


projekt.task_2()

print("-" * 50)

task_bar.remove("1/3")
task_bar.append("2/3")
print(f'TASK BAR{task_bar}')


print("-" * 50)


projekt.voting()


projekt.task_3()

print("-" * 50)

task_bar.remove("2/3")
task_bar.append("3/3")
print(f'TASK BAR{task_bar}')

print("-" * 50)

print("KONIEC GRY WSZYTKIE ZADANIA WYKOANE 3/3 GG")
print(f'Impostorem był kolor o numerze {projekt.impostor}')