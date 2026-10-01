# Basit To-Do List (Yapılacaklar Listesi) Uygulaması

import json
import os

# Veri dosyasının yolu
data_file = "todo_list.json"

# Yapılacaklar listesi için veri yapısı
todo_list = []

# JSON dosyasından verileri yüklen
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        todo_list = json.load(file)

# Yapılacaklar listesini kaydetme fonksiyonu
def save_tasks():
    with open(data_file, "w") as file:
        json.dump(todo_list, file, indent=4)

# Yapılacakları listeleme
def view_tasks():
    if not todo_list:
        print("\nYapılacak görev bulunamadı!\n")
    else:
        print("\nYapılacaklar Listesi:")
        for idx, task in enumerate(todo_list, 1):
            status = "Tamamlandı" if task['done'] else "Beklemede"
            print(f"{idx}. {task['task']} - [{status}]")
        print()

# Yeni görev ekleme
def add_task():
    task = input("Yeni görev girin: ")
    todo_list.append({"task": task, "done": False})
    save_tasks()
    print("Görev eklendi!\n")

# Görevi tamamlandı olarak işaretleme
def complete_task():
    view_tasks()
    task_num = int(input("Tamamlanan görev numarasını girin: "))
    if 0 < task_num <= len(todo_list):
        todo_list[task_num - 1]["done"] = True
        save_tasks()
        print("Görev tamamlandı olarak işaretlendi!\n")
    else:
        print("Geçersiz görev numarası!\n")

# Görev silme
def delete_task():
    view_tasks()
    task_num = int(input("Silmek istediğiniz görev numarasını girin: "))
    if 0 < task_num <= len(todo_list):
        removed_task = todo_list.pop(task_num - 1)
        save_tasks()
        print(f"'{removed_task['task']}' görevi silindi!\n")
    else:
        print("Geçersiz görev numarası!\n")

# Ana menü
def main():
    while True:
        print("""
        1. Yapılacakları Görüntüle
        2. Yeni Görev Ekle
        3. Görev Tamamla
        4. Görev Sil
        5. Çıkış
        """)

        choice = input("Bir seçenek girin (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen 1-5 arasında bir değer girin.\n")

if __name__ == "__main__":
    main()
