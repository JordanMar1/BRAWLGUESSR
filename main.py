import brawlstars as bs
import dotenv
import random
import json

dotenv.load_dotenv()

def get_random_brawler():
    """Ouvre le fichier brawlers.json et retourne un brawler au hasard"""
    with open("brawlers.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    brawler = random.choice(data)
    return brawler

brawler = get_random_brawler()
tries = 0
while True:
    if tries == 0:
        print(f"voici la rareté du brawler a deviner", brawler["rarity"])
    if tries == 1:
        print(f"voici le type du brawler a deviner", brawler["category"])
    if tries == 2:
        print(f"voici le nom de la star power du brawler a deviner", brawler["starPowers"][1]["name"])
    if tries == 3:
        print(f"voici le nom de la gadget du brawler a deviner", brawler["gadgets"][1]["name"])
    if tries == 4:
        print(f"voici le nom de la hyper charge du brawler a deviner", brawler["hyperCharges"][0]["name"])
    if tries == 5:
        print(f"voici le nom du brawler a deviner", brawler["name"][0])
    guess = input("Quel est le nom du brawler ? ")
    if guess.lower() == brawler["name"].lower():
        print("Bravo ! Vous avez deviné le brawler !")
        break
    if guess.lower() == "exit":
        print(f"Le brawler était {brawler['name']}")
        break
    else:
        print("Mauvaise réponse, essayez encore !")
        tries += 1
