import random
def main():
    mala = float(input"Ievadiet kvadrāta malas garumu: ")
    
    while True:
        print(f"Kvadrāta laukums ir{mala * mala} ")
        parb = input("Vai turpināt? y - jā, n - nē")
        if parb.lower() == "n" :
            break
 
if __name__ == "__main__":
    main()
