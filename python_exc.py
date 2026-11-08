
uzytkownik_A = {"odczyt", "zapis", "drukowanie"}
uzytkownik_B = {"odczyt", "usuwanie", "drukowanie"}


#A. Suma zbiorów (|)
#Zwraca wszystkie elementy z obu zbiorów, bez powtórzeń.
print('suma: ',uzytkownik_A | uzytkownik_B)


#B. Część wspólna (&)
#Zwraca tylko elementy, które występują w obu zbiorach.
print('część wspólna: ',uzytkownik_A & uzytkownik_B)

#C. Różnica zbiorów (-)
#Zwraca elementy, które znajdują się w pierwszym zbiorze, ale nie ma ich w drugim.
print('różnica zbiorów A - B: ',uzytkownik_A - uzytkownik_B)
print('różnica zbiorów B - A: ',uzytkownik_B - uzytkownik_A)

#D. Różnica symetryczna (^)
#Zwraca elementy, które występują tylko w jednym ze zbiorów, ale nie w obu jednocześnie.
print('różnica symetryczna: ',uzytkownik_A ^ uzytkownik_B)





