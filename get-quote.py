import random
def primary():    
    f = open("quotes.txt", 'r+')
    f.write("I am Renee \n")
    quotes = f.readlines()
    f.close()
    
    last = len(quotes)-1
    num_quotes = 2
    for i in range(num_quotes):
        rnd = random.randint(0, last)
        quote = quotes[rnd].rstrip("\n")
        print(quote)

if __name__== "__main__":
    primary()
