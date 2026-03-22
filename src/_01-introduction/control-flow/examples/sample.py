# owoce = ["jabłko", "banan", "wiśnia", 1, 2, 3, [11, 22, 33]]
#
# for owoc in owoce:
#     print(owoc)

# owoce = ["jabłko", "banan", "wiśnia"]
# for owoc in owoce:
#     print(owoc)
#     owoce.append("gruszka")

# for i, owoc in enumerate(owoce, start=1):
#     print(f"{i}. {owoc}")

# imiona = ["Ania", "Bartek"]
# wieki  = [25, 30]
# for imie, wiek in zip(imiona, wieki):
#     print(f"{imie} ma {wiek} lat")

# for i in range(5):
#     if i == 3:
#         continue    # pomiń i=3
#     if i == 7:
#         break       # zatrzymaj pętlę przy i=7
#     print(i)
# else:
#     # wykonuje się, jeśli pętla zakończyła się BEZ break
#     print("Pętla zakończona normalnie")

# punkt = (1,1)
#
# match punkt:
#     case (x, y) if x == y+1:
#         print("Środek układu")
#     case (x, 0):
#         print(f"Na osi X, x={x}")
#     case (0, y):
#         print(f"Na osi Y, y={y}")
#     case (1, 1):
#         print(f"Punkt ({x}, {y})")
#     case _:
#         print(f"Nic nie pasukje, punkt to ({punkt[0]}, {punkt[1]})")

# kwadraty = [x ** 2 for x in range(1, 6)]
# print(kwadraty)
# parzyste = [x for x in range(20) if x % 2 == 0]
# print(parzyste)
suma = sum(x ** 2 for x in range(1_000_000))
print(suma)