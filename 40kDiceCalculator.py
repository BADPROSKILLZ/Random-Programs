import random
import re

def matches_pattern_in_list(strings, pattern):
    """
    Checks if any string in the list contains the given pattern followed by a number and returns indices.
    
    :param strings: List of strings to check.
    :param pattern: The fixed part of the pattern (e.g., "rf ").
    :return: Tuple (bool, list of indices where the pattern was found).
    """
    regex = re.escape(pattern) + r"\d+"
    indices = [i for i, s in enumerate(strings) if re.search(regex, s)]
    
    return bool(indices), indices

def getKeywords(offOrDef, list):
    if offOrDef == "o":
        print("Indirect Fire = if, Melta X = m #, Twin-Linked = tl, Anti-x = anti #, Blast = b, Sustained Hits X = sus #, Devestating Wounds = dev, Rapid Fire X = rf #, Lethal Hits = lh, Lance = la, Heavy = he, Torrent = t, Hazardous = ha, Ignores Cover = ic, Hit Reroll 1s = hr1, Hit Reroll All = hra, \nWound Reroll 1s = wr1, Wound Reroll All = wra, Damage Reroll 1s = dr1, Damage Reroll All = dra, Critical Hit on X = crith #, Critical Wound on X = critw #")
    elif offOrDef == "d":
        print("Feel No Pain X = fnp #, +X to Saving Throw = save #, Cover = c, Stealth = st, +1 to req. Hit = h, +1 to req. Wound = w, Half Damage = hd")

    keyword = input("Enter a keyword (n/a to stop): ")
    while(keyword != "n/a"):
        global halfRange
        global move
        global charged
        global canSee
        list.append(keyword)
        match list[-1]: #Certain keywords have preconditions (heavy, melta, lance, rapid fire)
            case rf if re.fullmatch(r"rf \d+", rf): #Flat Rapid Fire
                q = input("Unit is within half range? (y or n) ")
                if q == "y": 
                    halfRange = True
                else: 
                    halfRange = False
            case rfd if re.fullmatch(r"rf \d+[a-zA-Z]?\d*", rfd): #Dice Rapid Fire
                q = input("Unit is within half range? (y or n) ")
                if q == "y": 
                    halfRange = True
                else: 
                    halfRange = False
            case mf if re.fullmatch(r"m \d+", rf): #Flat Melta
                q = input("Unit is within half range? (y or n) ")
                if q == "y": 
                    halfRange = True
                else: 
                    halfRange = False
            case mfd if re.fullmatch(r"rf \d+[a-zA-Z]?\d*", mfd): #Dice Melta
                q = input("Unit is within half range? (y or n) ")
                if q == "y": 
                    halfRange = True
                else: 
                    halfRange = False
            case "la":
                q = input("Did the attacking unit charge this turn? (y or n) ")
                if q == "y":
                    charged = True
                else:
                    charged = False
            case "he":
                q = input("Did the unit move this turn? (y or n) ")
                if q == "n":
                    move = False
                else:
                    move = True
            case "if":
                q = input("Can the attacking unit see the defending unit? (y or n) ")
                if q == "n":
                    canSee = False
                else: 
                    canSee = True
            case _:
                pass
            
        keyword = input("Enter a keyword (n/a to stop): ")
    
def calculateNumAttacks(): #FINISHED (Rapid Fire needs a change)
    totalAttacks = 0
    attackList = []
    global halfRange
    for j in range(numAttackers): #Calculate for each attacker
        try: 
            totalAttacks += int(numAttacks) #Flat Num of Attacks
            if halfRange: #Rapid Fire
                totalAttacks += int(numAttacks)
        except: 
            numDice = int(numAttacks[0:numAttacks.index("d")]) #Number of Dice
            if halfRange: #Rapid Fire
                numDice += int(numAttacks[0:numAttacks.index("d")])
                    
            try:
                if numAttacks.index("+")>=0: #Dice + Flat Attacks
                    diceType = int(numAttacks[numAttacks.index("d")+1:numAttacks.index("+")]) #Finding what type of die (d3, d6)
                    totalAttacks += int(numAttacks[numAttacks.index("+")+1:]) #Adding the flat attacks
            except:
                diceType = int(numAttacks[numAttacks.index("d")+1:]) #Finding what type of die (d3, d6)

            for i in range(numDice): #Rolling the dice
                dieRoll = random.randint(1, diceType)
                totalAttacks += dieRoll
                attackList.append(dieRoll)
    
        #KEYWORDS: Blast
        if "b" in offenseKeywords:
            totalAttacks += int(numDefenders/5)
        
    return totalAttacks, attackList    

def calculateHitReq(): #Keywords + Modifiers (DONE?)
    global moved
    global canSee
    appliedKeywords = []
    requiredHit = hitsOn
    requiredCrit = 6
    for i in allKeywords:
        match i:
            case "he": #Heavy
                if moved == False:
                    requiredHit -= 1 if requiredHit > 2 else 0
                    appliedKeywords.append(i)
            case "t": #Torrent
                requiredHit = 1
                appliedKeywords.append(i)
                break #No further changes to hit
            case crith if re.fullmatch(r"crith \d+", crith): #Crit Hit on X
                requiredCrit = crith[6:]
                appliedKeywords.append(crith)
            case "if":
                if canSee == False: #Indirect Fire without visibility is +1 to req. hit, Cover and fails on unmodified 1-3s
                    requiredHit += 1 if requiredHit < 6 else 0
                    requiredHit = 4 if requiredHit < 4 else requiredHit
                    appliedKeywords.append(i)
                    if "c" not in allKeywords:
                        allKeywords.append("c")
            case "st" | "h": #Stealth and/or S
                requiredHit += 1 if requiredHit < 6 else 0
                appliedKeywords.append(i)
    
    requiredHit = requiredCrit if requiredCrit < requiredHit else requiredHit
    
    return requiredHit, requiredCrit, appliedKeywords
                
def calculateWoundReq():
    pass

def calculateSaveReq():
    pass

def calculateTotalDamage():
    pass

halfRange: bool = False
moved: bool = True
charged: bool = False
canSee: bool = True
print("ATTACKING STATS:\n----------------------------------")
numAttackers = int(input("Attacking models: "))
numAttacks = input("Number of attacks: ")

hitsOn = int(input("BS/WS: "))
"""
strength = int(input("Strength: "))
armorPenetration = int(input("AP: "))
damage = input("Damage: ")
"""
offenseKeywords = []
getKeywords("o", offenseKeywords)
print(offenseKeywords)

print("\nDEFENDING STATS:\n----------------------------------")
numDefenders = int(input("Defending models: "))
"""
toughness = int(input("Toughness: "))
naturalSave = int(input("Save: "))
invul = int(input("Invulnerable Save: "))
wounds = int(input("Wounds: "))
"""
defenseKeywords = []
getKeywords("d", defenseKeywords)
print(defenseKeywords)

allKeywords = offenseKeywords + defenseKeywords
print(allKeywords)

#ATTACKS SECTION
DICEROLLS = 10000
sumAttacks = 0
for i in range(DICEROLLS):
    try:
        int(numAttacks) #Flat Attacks
        totalAttacks, attackList = calculateNumAttacks()
        sumAttacks += totalAttacks * DICEROLLS
        #print(totalAttacks, attackList)
        break
    except:
        totalAttacks, attackList = calculateNumAttacks()
        sumAttacks += totalAttacks
        #print(totalAttacks, attackList)
        
avgAttacks = int(sumAttacks/DICEROLLS)
print("Expected attacks: "+str(avgAttacks))

#HITS SECTION
hitList = []
reqHit, reqCrit, appliedKeywords = calculateHitReq()
sumHits = 0
lethals = 0
if reqHit == 1:
    sumHits = avgAttacks
else:
    for i in range(DICEROLLS):
        dieRoll = random.randint(1, 6)
        hitList.append(dieRoll)
        if dieRoll >= reqHit:
            sumHits += 1
            if dieRoll >= reqCrit:
                for i in allKeywords:
                    if re.fullmatch(r"sus (\d+|[1-9]\d*d[1-9]\d*)", i):
                        try:
                            i.index("d")
                            for j in range(i[i.index("d")-1]):
                                sumHits += random.randint(1, i[i.index("d")+1])
                        except:
                            sumHits += i[5:]
                    
                    if i == "lh":
                        lethals += 1
        else:
            if dieRoll == 1 and "hr1" in allKeywords:
                

