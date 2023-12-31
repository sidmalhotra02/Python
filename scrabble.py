letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zip_list = zip(letters, points)
letters_to_points = {letters:points for letters, points in zip_list}
# print(letters_to_points) check 1. 

letters_to_points[" "] = 0
# print(letters_to_points) check 2 

def score_word(word):
  point_total = 0
  for let in word:
    point_total += letters_to_points.get(let, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
players_to_points = {}

for player,words in player_to_words.items():
  player_points = 0 
  for word in words:
    player_points += score_word(word)
  players_to_points[player] = player_points


print(players_to_points)
