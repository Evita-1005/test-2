# Spēle - Uzmini skaitli

import random

def main():
    
    rnd = random.randint(1,9) 

    x = int(input("Uzmini skaiktli 1 līdz 9: "))
    count = 1

    while (x != rnd):
        count += 1
        x = int(input("Neuzminēji, mēģini vēlraiz, ievadi skaiktli 1 līdz 9: "))
    
    print(f" Apsveicam, tu uzzmunēji skaitli {x} ar {count} reizi!")
if __name__ == "__main__":
    main() 
