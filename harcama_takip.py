# KİŞİSEL HARCAMA TAKİP SİSTEMİ

import json
import os
from datetime import datetime

# Veri dosyasının yolu
data_file = "harcamalar.json"

# Harcama listesi için veri yapısı
expenses = []

# JSON dosyasından verileri yüklen
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        expenses = json.load(file)

# Verileri kaydetme fonksiyonu
def save_expenses():
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)

# Harcamaları listeleme
def view_expenses():
    if not expenses:
        print("\nHenüz bir harcama eklenmedi!\n")
    else:
        print("\nHarcama Listesi:")
        total = 0
        for idx, expense in enumerate(expenses, 1):
            print(f"{idx}. {expense['tarih']} - {expense['kategori']} - {expense['aciklama']} - {expense['miktar']} TL")
            total += expense['miktar']
        print(f"\nToplam Harcama: {total} TL\n")

# Yeni harcama ekleme
def add_expense():
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    kategori = input("Kategori (Gıda, Ulasım, Eğlence, vb.): ")
    aciklama = input("Açıklama: ")
    try:
        miktar = float(input("Miktar (TL): "))
    except ValueError:
        print("Geçersiz miktar! Lütfen sayı girin.\n")
        return

    expenses.append({
        "tarih": tarih,
        "kategori": kategori,
        "aciklama": aciklama,
        "miktar": miktar
    })
    save_expenses()
    print("Harcama başarıyla eklendi!\n")

# Harcama silme
def delete_expense():
    view_expenses()
    try:
        idx = int(input("Silmek istediğiniz harcamanın numarasını girin: "))
        if 0 < idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            save_expenses()
            print(f"'{removed['aciklama']}' harcaması silindi!\n")
        else:
            print("Geçersiz numara!\n")
    except ValueError:
        print("Geçersiz giriş!\n")

# Ana menü
def main():
    while True:
        print("""
        1. Harcamaları Görüntüle
        2. Yeni Harcama Ekle
        3. Harcama Sil
        4. Çıkış
        """)

        choice = input("Bir seçenek girin (1-4): ")

        if choice == '1':
            view_expenses()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen 1-4 arasında bir değer girin.\n")

if __name__ == "__main__":
    main()
