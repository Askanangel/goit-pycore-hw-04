def get_cats_info(path):
    cats_info = []
    try:
        with open (path, encoding='utf-8') as file:
            for line in file:
                cat = line.split (",")
                id = cat[0]
                name = cat[1]
                age = float (cat[2])
                cats_info.append ({"id_cat":id,
                              "name_cat":name,
                              "age_cat":age})
    except FileNotFoundError: 
            print("Файл не знайдено")
    return cats_info
cats = get_cats_info ("cat_info.txt")
print (cats)