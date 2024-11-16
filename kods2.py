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
