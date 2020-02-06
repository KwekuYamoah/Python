def dol(amt):
    dollars = amt/5.28
    return dollars
def pod(amt):
    pounds = amt/6.78
    return pounds
def eur(amt):
    euros = amt/5.95
    return euros
def main():
    money = float(input("Enter your amount in Ghana cedis:\n"))
    outfile = open("Converter.txt","w")
    print(money, "ghc in dollars is:" , dol(money), file=outfile)
    print(money, "ghc in pounds is " , pod(money), file=outfile)
    print(money, "ghc in euros is:" , eur(money), file=outfile)
main()
    