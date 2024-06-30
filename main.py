# this program is a Star Wars themed Top Trumps.
# there are 60 cards but a maximum of 30 are used per game.
# the program lets the choosing player choose
  # and then tells the players who won with what card.
# the cards are transferred and the winning player goes next
  # in case of a draw the cards are stored in a carry for the next winner.

# yes. there's a _bit_ of code, sorry.
# p.s. the attributes are my opinion - yep
class players():
  # creating a class for the players: they each have a name and cards
  def __init__(self, name):
    self.name = name
    self.cards = []



class trumps():
  # creating a class for the cards: all their attributes are here
  def __init__(self, name, affiliation, height, force, agility, wisdom, rating):
    self.name = name
    self.affiliation = affiliation
    self.height = height
    self.force = force
    self.agility = agility
    self.wisdom = wisdom
    self.rating = rating



class frequency():
  # for working out the most picked attribute
  def __init__(self, name):
    self.name = name
    self.freq = 0



def trumpsCreation():
  # all the cards created using the class trumps()
  # neat layout so I can make the attributes fair depending on others

  #char0 = trumps("name", "affiliation", "height", "force/10", "agility/25", "wisdom/50", "rating/100")
  #                 n                      a                h    f   a   w    r
  char01 = trumps("Mando",             "*Top Trump*",     1.80,  0, 19, 34, 100)
  char02 = trumps("The Child",         "_redacted_",      0.34,  3, 19, 22,  99)
  char03 = trumps("Luthen Rael",       "Rebel Alliance",  1.90,  0, 10, 47,  98)
  char04 = trumps("Boba Fett",         "Bounty Hunter",   1.83,  0, 10, 38,  97)
  char05 = trumps("Yoda",              "Jedi",            0.66,  9, 24, 50,  96)
  char06 = trumps("Fennec Shand",      "Assassin",        1.63,  0, 22, 34,  96)
  char07 = trumps("Ahsoka Tano",       "Jedi/Unaligned",  1.70,  7, 23, 35,  92)
  char08 = trumps("Wicket Warrick",    "Ewok",            0.80,  0, 15, 10,  91)
  char09 = trumps("Qui-Gon Jinn",      "Jedi",            1.93,  5,  6, 48,  90)
  char10 = trumps("Han Solo",          "Rebel Alliance",  1.83,  0, 20, 30,  88)

  char11 = trumps("Darth Vader",       "Galactic Empire", 2.03, 10,  4, 20,  86)
  char12 = trumps("Kino Loy",          "Floor Manager",   1.73,  0, 12, 40,  85)
  char13 = trumps("Kuiil",             "Engineer",        1.45,  0,  5, 48,  82)
  char14 = trumps("Thrawn",            "Empire",          1.95,  0, 17, 49,  81)
  char15 = trumps("Sabine Wren",       "Rebel",           1.70,  0, 22, 10,  80)
  char16 = trumps("Peli Motto",        "Ship Engineer",   1.55,  0, 10, 29,  71)
  char17 = trumps("The Armorer",       "Mandalorian",     1.70,  0, 18, 41,  79)
  char18 = trumps("Cara Dune",         "Resistance",      1.73,  0, 19, 20,  78)
  char19 = trumps("Greef Karga",       "BH's Guild",      1.88,  0, 14, 37,  78)
  char20 = trumps("IG-11",             "Droid",           2.19,  0, 21,  0,  78)

  char21 = trumps("Chirrut Îmwe",      "Guardian",        1.73,  1, 23, 25,  76)
  char22 = trumps("Darth Maul",        "Sith Lord",       1.75,  5, 25, 20,  75)
  char23 = trumps("Jar Jar Binks",    "_undercover_ Sith",1.96, 11, 11, 11,  70)
  char24 = trumps("Count Dooku",       "Separatist",      1.93,  8,  6, 45,  65)
  char25 = trumps("Chewbacca",         "Rebel Alliance",  2.28,  0, 11,  5,  64)
  char26 = trumps("Obi-Wan Kenobi",    "Jedi",            1.75,  7,  8, 44,  63)
  char27 = trumps("Luke Skywalker",    "Jedi",            1.72,  8, 21, 25,  62)
  char28 = trumps("Princess Leia",     "Rebel Alliance",  1.52,  3, 19, 41,  62)
  char29 = trumps("Yaddle",            "Jedi",            0.61,  7, 20, 40,  59)
  char30 = trumps("Kylo Ren",          "Knights of Ren",  1.90,  6, 16, 25,  58)

  char31 = trumps("Cassian Andor",     "Rebel Alliance",  1.78,  0, 11, 15,  50)
  char32 = trumps("Admiral Ackbar",    "Rebel Alliance",  1.80,  0, 10, 44,  50)
  char33 = trumps("Ezra Bridge",       "Rebel",           1.65,  6, 24, 17,  48)
  char34 = trumps("R2-D2",             "Droid",           1.09,  0, 15,  0,  45)
  char35 = trumps("C-3PO",             "Droid",           1.67,  0,  1,  0,  44)
  char36 = trumps("General Grievous",  "Separatist",      2.16,  0,  5,  0,  43)
  char37 = trumps("Jango Fett",        "Bounty Hunter",   1.83,  0, 21, 25,  42)
  char38 = trumps("Sheev Palpatine",   "Galactic Empire", 1.73,  9,  2, 40,  40)
  char39 = trumps("Lando Calrissian",  "Rebel Alliance",  1.78,  0, 12, 15,  37)
  char40 = trumps("Finn",              "Rebel Alliance",  1.80,  0, 12, 26,  37)

  char41 = trumps("Mace Windu",        "Jedi",            1.88,  6,  7, 35,  36)
  char42 = trumps("Padmé Amidala",     "Republic",        1.65,  1,  9, 32,  36)
  char43 = trumps("Rex",               "Clone Trooper",   1.83,  0, 15, 30,  35)
  char44 = trumps("Baze Malbus",       "Guardian",        1.80,  0, 16, 24,  35)
  char45 = trumps("Moff Gideon",       "Empire",          1.73,  0, 16, 24,  32)
  char46 = trumps("Cad Bane",          "Bounty Hunter",   1.00,  0, 12, 47,  31)
  char47 = trumps("Bo-Katan Kryze",    "Mandalorian",     1.80,  0, 22, 36,  30)
  char48 = trumps("Enfys Nest",        "Cloud Rider",     1.87,  0, 19, 22,  29)
  char49 = trumps("Hondo Ohnaka",      "Pirate",          1.85,  0, 11, 38,  28)
  char50 = trumps("Ki-Adi Mundi",      "Jedi",            1.98,  5, 12, 36,  27)

  char51 = trumps("Rey",               "Rebel Alliance",  1.70,  4, 12, 20,  26)
  char52 = trumps("Maz Katana",        "Resistance",      1.24,  0,  4, 45,  25)
  char53 = trumps("Mon Mothma",        "Rebel Alliance",  1.50,  0,  5, 39,  20)
  char54 = trumps("Poe Dameron",       "Rebel Alliance",  1.72,  0, 10, 20,  18)
  char55 = trumps("BB-8",              "Droid",           0.67,  0, 20,  0,  17)
  char56 = trumps("Paz Vizsla",        "Mandalorian",     1.91,  0, 16, 25,  16)
  char57 = trumps("Max Rebo",          "Musisician",      1.50,  0,  9, 20,  13)
  char58 = trumps("Captain Phasma",    "First Order",     2.01,  0, 11, 23,  10)
  char59 = trumps("Snoke",             "Dark Side",       2.13,  3,  1, 22,   5)
  char60 = trumps("Jabba the Hutt",    "Crime Lord",      1.75,  0,  0, 10,   0)

  # cards are in a list so that they can be dealt
  global cards
  cards = [char01, char02, char03, char04, char05, char06, char07, char08, char09, char10, char11, char12, char13, char14, char15, char16, char17, char18, char19, char20, char21, char22, char23, char24, char25, char26, char27, char28, char29, char30, char31, char32, char33, char34, char35, char36, char37, char38, char39, char40, char41, char42, char43, char44, char45, char46, char47, char48, char49, char50, char51, char52, char53, char54, char55, char56, char57, char58, char59, char60]
  # cards are shuffled
  endRange = random.randint(6, 13)
  for i in range(0, endRange):
    random.shuffle(cards)
    random.shuffle(cards)



def playerCreation():
  # players are created here using the class players()
  global playerNum
  playerNum = input("how many players (2-6): ")
  while playerNum != "2" and playerNum != "3" and playerNum != "4" and playerNum != "5" and playerNum !=  "6":
    playerNum = input("how many players, IN THE RANGE 2-6 (inclusive): ")
  playerNum = int(playerNum)
  global player1
  global player2
  global player3
  global player4
  global player5
  global player6
  # for 2 players, only this runs
  if playerNum >= 2:
    player1Name = input("enter name of player 1: ")
    player2Name = input("enter name of player 2: ")
    player1 = players(player1Name)
    player2 = players(player2Name)
    allPlayers.append(player1)
    allPlayers.append(player2)
  if playerNum >= 3:
    player3Name = input("enter name of player 3: ")
    player3 = players(player3Name)
    allPlayers.append(player3)
  if playerNum >= 4:
    player4Name = input("enter name of player 4: ")
    player4 = players(player4Name)
    allPlayers.append(player4)
  if playerNum >= 5:
    player5Name = input("enter name of player 5: ")
    player5 = players(player5Name)
    allPlayers.append(player5)
  # for 6 players, all of them would run
  if playerNum >= 6:
    player6Name = input("enter name of player 6: ")
    player6 = players(player6Name)
    allPlayers.append(player6)



def frequencyCreation():
  global fHeight
  global fForce
  global fAgility
  global fWisdom
  global fRating
  fHeight = frequency("Height")
  fForce = frequency("Force")
  fAgility = frequency("Agility")
  fWisdom = frequency("Wisdom")
  fRating = frequency("Rating")


  
def dealCards():
  # the cards are dealt to each player

  # not all cards are used for 4-6 players so that
  # every player has the same number of cards
  cardsPerP = 30 // playerNum
  print(f"{Fore.BLACK}game loading, {Fore.YELLOW}{Style.BRIGHT}{cardsPerP} {Style.RESET_ALL}{Fore.BLACK}cards per player.{Fore.RESET}\n")
  # adding the first item of cards to the player's cards
  # and deleting that first item from cards
  for j in range(0,cardsPerP):
    player1.cards.append(cards[0])
    cards.pop(0)
    player2.cards.append(cards[0])
    cards.pop(0)
    if playerNum >= 3:
      player3.cards.append(cards[0])
      cards.pop(0)
    if playerNum >= 4:
      player4.cards.append(cards[0])
      cards.pop(0)
    if playerNum >= 5:
      player5.cards.append(cards[0])
      cards.pop(0)
    if playerNum >= 6:
      player6.cards.append(cards[0])
      cards.pop(0)



def gamePlay():
  # this is for the first round of play

  # picking the starting player randomly
  startingN = random.randrange(0,playerNum)
  startingP = allPlayers[startingN]
  print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}is {Fore.MAGENTA}starting{Fore.RESET}.")
  # printing the card out
  print("Your card: \n")
  print(f"Name: {Fore.CYAN}{startingP.cards[0].name}{Fore.RESET}")
  print(f"Affiliation: {startingP.cards[0].affiliation} (info)")
  print(f"Height: {Fore.CYAN}{startingP.cards[0].height}{Fore.RESET} (/m)")
  print(f"Force: {Fore.CYAN}{startingP.cards[0].force}{Fore.RESET} /10")
  print(f"Agility: {Fore.CYAN}{startingP.cards[0].agility}{Fore.RESET} /25")
  print(f"Wisdom: {Fore.CYAN}{startingP.cards[0].wisdom}{Fore.RESET} /50")
  print(f"Rating: {Fore.CYAN}{startingP.cards[0].rating}{Fore.RESET} /100\n")

  # asking for the player to pick an attribute
  choice = input(f"Pick an attribute ({Fore.CYAN}H{Fore.RESET}/{Fore.CYAN}F{Fore.RESET}/{Fore.CYAN}A{Fore.RESET}/{Fore.CYAN}W{Fore.RESET}/{Fore.CYAN}R{Fore.RESET}): ")
  # the choice is made capital so that more options are possible
  # ie h / H / height / HeIgHt
  choice = choice.upper()
  while choice != "H" and choice != "F" and choice != "A" and choice != "W" and choice != "R" and choice != "HEIGHT" and choice != "FORCE" and choice != "AGLILITY" and choice != "WISDOM" and choice != "RATING":
    choice = input(f"Pick an attribute out of:\n {Fore.CYAN}H(height){Fore.RESET}/{Fore.CYAN}F(force){Fore.RESET}/{Fore.CYAN}A(agility){Fore.RESET}/{Fore.CYAN}W(wisdom){Fore.RESET}/{Fore.CYAN}R(rating){Fore.RESET}: ")
    choice = choice.upper()
  # the responding players are all the players except the
  # player that chooses the attribute
  respondingPlayers = []
  for i in range(0,len(allPlayers)):
    respondingPlayers.append(allPlayers[i])
  respondingPlayers.remove(startingP)
  global winner
  global contest
  global carry
  winner = ""
  contest = []
  carry = []
  draw = False

  # if the attribute chosen is height then;
  if choice == "H" or choice == "HEIGHT":
    fHeight.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Height, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a height of {Fore.CYAN}{startingP.cards[0].height}{Fore.RESET}")
    # the contest happens (who is tallest?)
    contest.append(startingP.cards[0].height)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].height)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a height of {Fore.CYAN}{respondingPlayers[i].cards[0].height}{Fore.RESET}")
    print("\n")
    # if there is only 1 winner;
    if contest.count(max(contest)) == 1:
      # if the winner is the starting player;
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        # who won then?
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, height {Fore.CYAN}{winner.cards[0].height}{Fore.RESET}\n")
    else:
      # 2 or more players have the same attribute
      # (and that attribute is the heighest)
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True

  # same here but for force then agility, wisdom and rating
  elif choice == "F" or choice == "FORCE":
    fForce.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Force, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a force of {Fore.CYAN}{startingP.cards[0].force}{Fore.RESET}")
    contest.append(startingP.cards[0].force)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].force)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a force of {Fore.CYAN}{respondingPlayers[i].cards[0].force}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, force {Fore.CYAN}{winner.cards[0].force}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True

  elif choice == "A" or choice == "AGILITY":
    fAgility.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Agility, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has an agility of {Fore.CYAN}{startingP.cards[0].agility}{Fore.RESET}")
    contest.append(startingP.cards[0].agility)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].agility)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with an agility of {Fore.CYAN}{respondingPlayers[i].cards[0].agility}{Fore.RESET}") 
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, agility {Fore.CYAN}{winner.cards[0].agility}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True
    
  elif choice == "W" or choice == "WISDOM":
    fWisdom.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Wisdom, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a wisdom of {Fore.CYAN}{startingP.cards[0].wisdom}{Fore.RESET}")
    contest.append(startingP.cards[0].wisdom)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].wisdom)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a wisdom of {Fore.CYAN}{respondingPlayers[i].cards[0].wisdom}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, wisdom {Fore.CYAN}{winner.cards[0].wisdom}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True
    
  elif choice == "R" or choice == "RATING":
    fRating.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Rating, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a rating of {Fore.CYAN}{startingP.cards[0].rating}{Fore.RESET}")
    contest.append(startingP.cards[0].rating)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].rating)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a rating of {Fore.CYAN}{respondingPlayers[i].cards[0].rating}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, rating {Fore.CYAN}{winner.cards[0].rating}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True

  
  if draw == True:
    # the cards are held in the carry in case of a tie
    # do that they can be won next round
    # (unless it's a tie again, then the carry just becomes bigger)
    for i in range(0,len(allPlayers)):
      carry.append(allPlayers[i].cards[0])
      allPlayers[i].cards.pop(0)
    winner = startingP
    print(f"{Fore.GREEN}cards placed in the centre for next round{Fore.RESET}\n")
  else:
    # the cards are given to the winner
    # (and removed from the others, no duplicates!)
    for i in range(0,len(allPlayers)):
      winner.cards.append(allPlayers[i].cards[0])
      allPlayers[i].cards.pop(0)
    print(f"{Fore.GREEN}cards transferred to {winner.name}{Fore.RESET}\n")



def endPlay():
  # this is the body of the program
  # it is basically the same as gamePlay()
  # but it is adapted so that it can run again
  # until the end of the game
  global winner
  global contest
  global carry
  # the starting player is no longer random
  # (the winner in a draw is the startingP from 
  # previous round, see line 285)
  startingP = winner
  for i in range(0,len(allPlayers)):
    # (I will talk about the colours at the end of the code)
    print(f"{allPlayers[i].name} has {Fore.YELLOW}{Style.BRIGHT}{len(allPlayers[i].cards)}{Style.RESET_ALL}{Fore.RESET} cards")
  print(f"\n{Fore.BLUE}{startingP.name} {Fore.RESET}with {Fore.YELLOW}{len(startingP.cards)} {Fore.RESET}cards is {Fore.MAGENTA}choosing{Fore.RESET}.")
  print("Your card: \n")
  print(f"Name: {Fore.CYAN}{startingP.cards[0].name}{Fore.RESET}")
  print(f"Affiliation: {startingP.cards[0].affiliation} (info)")
  print(f"Height: {Fore.CYAN}{startingP.cards[0].height}{Fore.RESET} (/m)")
  print(f"Force: {Fore.CYAN}{startingP.cards[0].force}{Fore.RESET} /10")
  print(f"Agility: {Fore.CYAN}{startingP.cards[0].agility}{Fore.RESET} /25")
  print(f"Wisdom: {Fore.CYAN}{startingP.cards[0].wisdom}{Fore.RESET} /50")
  print(f"Rating: {Fore.CYAN}{startingP.cards[0].rating}{Fore.RESET} /100\n")
  
  choice = input(f"Pick an attribute ({Fore.CYAN}H{Fore.RESET}/{Fore.CYAN}F{Fore.RESET}/{Fore.CYAN}A{Fore.RESET}/{Fore.CYAN}W{Fore.RESET}/{Fore.CYAN}R{Fore.RESET}): ")
  choice = choice.upper()
  while choice != "H" and choice != "F" and choice != "A" and choice != "W" and choice != "R" and choice != "HEIGHT" and choice != "FORCE" and choice != "AGLILITY" and choice != "WISDOM" and choice != "RATING":
    choice = input(f"Pick an attribute out of:\n {Fore.CYAN}H(height){Fore.RESET}/{Fore.CYAN}F(force){Fore.RESET}/{Fore.CYAN}A(agility){Fore.RESET}/{Fore.CYAN}W(wisdom){Fore.RESET}/{Fore.CYAN}R(rating){Fore.RESET}): ")
    choice = choice.upper()

  respondingPlayers = []
  for i in range(0,len(allPlayers)):
    respondingPlayers.append(allPlayers[i])
  respondingPlayers.remove(startingP)
  winner = ""
  contest = []
  draw = False

  # same as above
  if choice == "H" or choice == "HEIGHT":
    fHeight.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Height, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a height of {Fore.CYAN}{startingP.cards[0].height}{Fore.RESET}")
    contest.append(startingP.cards[0].height)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].height)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a height of {Fore.CYAN}{respondingPlayers[i].cards[0].height}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, height {Fore.CYAN}{winner.cards[0].height}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True

  elif choice == "F" or choice == "FORCE":
    fForce.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Force, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a force of {Fore.CYAN}{startingP.cards[0].force}{Fore.RESET}")
    contest.append(startingP.cards[0].force)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].force)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a force of {Fore.CYAN}{respondingPlayers[i].cards[0].force}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, force {Fore.CYAN}{winner.cards[0].force}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True

  elif choice == "A" or choice == "AGILITY":
    fAgility.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Agility, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has an agility of {Fore.CYAN}{startingP.cards[0].agility}{Fore.RESET}")
    contest.append(startingP.cards[0].agility)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].agility)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with an agility of {Fore.CYAN}{respondingPlayers[i].cards[0].agility}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, agility {Fore.CYAN}{winner.cards[0].agility}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True
    
  elif choice == "W" or choice == "WISDOM":
    fWisdom.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Wisdom,{Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a wisdom of {Fore.CYAN}{startingP.cards[0].wisdom}{Fore.RESET}")
    contest.append(startingP.cards[0].wisdom)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].wisdom)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a wisdom of {Fore.CYAN}{respondingPlayers[i].cards[0].wisdom}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, wisdom {Fore.CYAN}{winner.cards[0].wisdom}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True
    
  elif choice == "R" or choice == "RATING":
    fRating.freq += 1
    print(f"{Fore.BLUE}{startingP.name} {Fore.RESET}chooses Rating, {Fore.CYAN}{startingP.cards[0].name} {Fore.RESET}has a rating of {Fore.CYAN}{startingP.cards[0].rating}{Fore.RESET}")
    contest.append(startingP.cards[0].rating)
    for i in range(0,len(respondingPlayers)):
      contest.append(respondingPlayers[i].cards[0].rating)
      print(f"{Fore.BLUE}{respondingPlayers[i].name} {Fore.RESET}has {Fore.CYAN}{respondingPlayers[i].cards[0].name} {Fore.RESET}with a rating of {Fore.CYAN}{respondingPlayers[i].cards[0].rating}{Fore.RESET}")
    print("\n")
    if contest.count(max(contest)) == 1:
      if contest.index(max(contest)) == 0:
        winner = startingP
      else:
        winner = respondingPlayers[contest.index(max(contest))-1]
      print(f"{Fore.RED}{winner.name} wins {Fore.RESET}with {Fore.CYAN}{winner.cards[0].name}{Fore.RESET}, rating {Fore.CYAN}{winner.cards[0].rating}{Fore.RESET}\n")
    else:        
      print(f"{Fore.RED}there is a draw, next round loading{Fore.RESET}\n")
      draw = True

  else:
    print("choice not validated. ")
  
  if draw == True:
    for i in range(0,len(allPlayers)):
      carry.append(allPlayers[i].cards[0])
      allPlayers[i].cards.pop(0)
    winner = startingP
    print(f"{Fore.GREEN}cards placed in the centre for next round{Fore.RESET}\n")
  else:
    print(f"{Fore.GREEN}cards transferred to {winner.name}{Fore.RESET}\n")
    if carry != []:
      for i in range(0,len(carry)):
        winner.cards.append(carry[0])
        carry.pop(0)
    for i in range(0,len(allPlayers)):
      winner.cards.append(allPlayers[i].cards[0])
      allPlayers[i].cards.pop(0)

  noCards = []
  # now it changes:
  for i in range(0,len(allPlayers)):
    # if they have no cards left
    if len(allPlayers[i].cards) == 0: 
      noCards.append(allPlayers[i])
  for i in range(0,len(noCards)):
    allPlayers.remove(noCards[i])
    print(f"{Fore.RED}{noCards[i].name} has no more cards and is out of the game{Fore.RESET}\n")

  if len(allPlayers) == 1:
    # well done {allPlayers[0].name}!
    print(f"{Fore.RED}{allPlayers[0].name} {Fore.GREEN}h{Fore.BLUE}a{Fore.MAGENTA}s {Fore.YELLOW}a{Fore.CYAN}l{Fore.GREEN}l {Fore.BLUE}t{Fore.MAGENTA}h{Fore.YELLOW}e {Fore.CYAN}c{Fore.GREEN}a{Fore.BLUE}r{Fore.MAGENTA}d{Fore.YELLOW}s {Fore.CYAN}a{Fore.GREEN}n{Fore.BLUE}d {Fore.RED}WINS!!!{Fore.RESET}{Style.RESET_ALL}\n")
    freqNAMES = [fHeight.name, fForce.name, fAgility.name, fWisdom.name, fRating.name]
    freqNUMS = [fHeight.freq, fForce.freq, fAgility.freq, fWisdom.freq, fRating.freq]
    if freqNUMS.count(max(freqNUMS)) == 1:
      print(f"{Fore.BLACK}the most picked attribute was: {Fore.YELLOW}{Style.BRIGHT}{freqNAMES[freqNUMS.index(max(freqNUMS))]} {Style.RESET_ALL}{Fore.BLACK}(with {max(freqNUMS)} picks).{Fore.RESET}")
    else:
      mostFrequent = []
      for i in range(0,len(freqNUMS)):
        if freqNUMS[i] == max(freqNUMS):
          mostFrequent.append(freqNAMES[i])
      print(f"{Fore.BLACK}the most picked attributes were: ")
      for i in range(0,len(mostFrequent)):
        print(f"{Fore.YELLOW}{Style.BRIGHT}{mostFrequent[i]}{Style.RESET_ALL}{Fore.RESET}")
      print(f"{Fore.BLACK}(with {max(freqNUMS)} picks).{Fore.RESET}")
      quit()

  # runs another round!
  else:
    endPlay()



def quit():
  # thanks for playing
  print(f"\n{Fore.BLACK}end of game.{Fore.RESET}")



def main():
  # all the functions run here!
  trumpsCreation()
  playerCreation()
  frequencyCreation()
  dealCards()
  gamePlay()
  endPlay()



if __name__ == "__main__":
  # this runs if the name of the module is "main"
  # (it is :)

  import random
  # colorama is the easiest way I've found 
  # to print in colour: 
  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
  # to print something in colour:
  # print(f"{Fore.RED}this is red {Fore.BLUE}blue {Fore.RESET)back to white")
  import colorama
  from colorama import Fore, Style
  allPlayers = []
  main()
