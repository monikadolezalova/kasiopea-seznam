ulohy=int(input())
for i in range (ulohy):
    cena=int(input())
    mince=input()
    list = mince.split()
    kolik_mam_penez = 1 * int(list[0]) + 2 * int(list[1]) + 5 * int(list[2]) + 10 * int(list[3]) + 20 * int(list[4]) + 50 * int(list[5])
    if kolik_mam_penez >= cena:
        print("ANO")
    else:
        print("NE")