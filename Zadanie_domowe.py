# ZADANIE 11
# Stwórz słownik używając dictionary comprehension, gdzie klucze to liczby od 1 do 20, a
# wartości to ich kwadraty. Następnie przefiltruj ten słownik (też comprehension!) by zawierał
# tylko liczby parzyste.
# Wymagania:
  
# Użyj dictionary comprehension 2 razy

# Pierwszy słownik: wszystkie liczby 1-20

# Drugi słownik: tylko parzyste klucze
    
# Dwa słowniki wypisane

print(f"WSZYSTKO")
klucze_slownika = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
kwadraty_zad9 = {i: i**2 for i in klucze_slownika}
print(kwadraty_zad9)
print(f"\nNIEPARZYSTE")
kwadraty_zad9_bis = {i: i**2 for i in klucze_slownika if i % 2 ==0}
print(kwadraty_zad9_bis)

print(f"\nNIEPARZYSTE PO POPRAWCE")
kwadraty_zad9_bis = {j: k for j, k in kwadraty_zad9_bis.items() if j % 2 ==0}
print(kwadraty_zad9_bis)