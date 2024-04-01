jack = '''
╔╗ ╦  ╔═╗╔═╗╦╔═ ╦╔═╗╔═╗╦╔═
╠╩╗║  ╠═╣║  ╠╩╗ ║╠═╣║  ╠╩╗
╚═╝╩═╝╩ ╩╚═╝╩ ╩╚╝╩ ╩╚═╝╩ ╩
'''
welcome = "\nWelcome to Blackjack!\nThis is a card game with a single objective: beat the dealer’s hand without exceeding 21.\n>> You have ₹1000 to play with. \n>> You can bet 200, 100 or 50. \n\n"

cards = {
  13: '''
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- 
 ''',
  12: '''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- 
 ''',
  11: '''
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- 
 ''',
  10: '''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- 
 ''',
  9: '''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- 
 ''',
  8: '''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- 
 ''',
  7: '''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- 
 ''',
  6: '''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- 
 ''',
  5: '''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- 
 ''',
  4: '''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- 
 ''',
  3: '''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- 
 ''',
  2: '''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- 
 ''',
  1: '''
 -------
|A      |
|       |
|       |
|       |
|      A|
 ------- 
 '''
}


blanks = '''
 -------
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
 ------- '''