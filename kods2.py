
"""
Lietotājam jāmin gadījuma skaitlis no 1 līdz 10. Lietotājam ir dots ierobežots mēģinājumu skaits 3. 
Ja lietotājs uzmin skaitli, spēle informē par uzvaru, pretējā gadījumā, ja mēģinājumi beigušies, spēle informē par zaudējumu.

lai redzētu, kāds ir random sakaitlis pēc 0 rindas raksta print(f"{rnd=}")

"""


import random
def main():
    rnd = random.randint(1, 10)
    count = 3
    print(f"Jums ir {count} mēģinājumi, lai uzminētu skaitli.")
    while  count > 0:
        gues =  int(input("Miniet skaitli no 1 -10: "));
        if  gues == rnd:
            print("Apsveicu! Jūs uzminējās. pareizeis skaitlis ir {rnd}")
            break
        count -= 1
    else:
        print(f"Diemzēļ Jūs neuzminējāt, pareizais skaitlis bija {rnd}")

if __name__ == "__main__":
    main()
