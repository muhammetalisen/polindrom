def palindrom_mu(kelime):
    # Kelimeyi küçük harfe çevir ve boşlukları temizle
    kelime = kelime.lower().replace(" ", "")
    # Kelimeyi ters çevir
    ters_kelime = kelime[::-1]
    # Orijinal kelime ile ters kelimeyi karşılaştır
    return kelime == ters_kelime

def palindrom_kontrol():
    kelime = input("Bir kelime girin: ")
    if palindrom_mu(kelime):
        print(f"'{kelime}' bir palindromdur.")
    else:
        print(f"'{kelime}' bir palindrom değildir.")

palindrom_kontrol()
