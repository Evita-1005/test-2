def main():

    parole = "Parole123"
    reize = 3

    while reize > 0: 
        ievadita_parole = input("Ievadi paroli: ")
        reize -= 1
        if parole == ievadita_parole:
            print("Laipni lūdzam!")
            break
        else:
            print("Nepareiza parole.")
    else:
        print("Piekļuve liegta. Mēģinājumu skaits pārsniegts")
        
    
 
if __name__ == "__main__":
    main()
