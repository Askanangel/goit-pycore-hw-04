def total_salary(path):
    total = 0
    count = 0
    try:
        with open (path, encoding='utf-8') as file:
            for line in file:
                people=line.split(',')
                salary = float(people [1])
                total += salary
                count+=1
                avarage = total/count
            print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avarage}")

    except FileNotFoundError: 
            print("Файл не знайдено")

total_salary ("salary_all.txt")