en_ru_path = os.path.join(os.getcwd(), "lab_10", "103.txt")
ru_en_path = os.path.join(os.getcwd(), "lab_10", "ru_en.txt")

eng_dict = {}
ru_dict = {}

try:
    with open(en_ru_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            (eng_w_str, ru_w_str) = line.split(" - ")
            ru_words = ru_w_str.replace("\n", "").split(", ")
            eng_dict[eng_w_str] = ru_words

            for rw in ru_words:
                if rw in ru_dict:
                    ru_dict[rw].append(eng_w_str)
                else:
                     ru_dict[rw] = [eng_w_str]

    with open(ru_en_path, "w+", encoding="utf-8") as f:
        for ru_w, eng_w in sorted(ru_dict.items()):
            f.write(f"{ru_w} - {', '.join(eng_w)}\n")

except OSError:103.txt
    print("[ОШИБКА] Проблемы с файлом.")