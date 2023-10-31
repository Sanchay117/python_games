import random,time

suits=("Diamonds","Hearts","Clubs","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Card:

	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
		self.value=values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:

	def __init__(self):
		l=[]
		for suit in suits:
			for rank in ranks:
				l.append(Card(suit,rank))
		self.all_cards=l

	def shuffle(self):
		random.shuffle(self.all_cards)

	def print_deck(self):
		for card in self.all_cards:
			print(card)

	def deal_one(self):
		return self.all_cards.pop()

class Player:
	def __init__(self,name):
		self.name=name
		self.all_cards=[]
	def remove_one(self):
		return self.all_cards.pop(0) # Removing the top card (beginning of the list)
	def add_cards(self,new_cards):
		if type(new_cards)==type([]):
			# for multiple cards
			self.all_cards.extend(new_cards)
		else:
			# for single card
			self.all_cards.append(new_cards)
	def __str__(self):
		return f'Player {self.name} has {len(self.all_cards)} cards.'
	def shuffle(self):
		random.shuffle(self.all_cards)

def win():
	if p1.all_cards==[]:
		print("Player 2 WINS!")
		exit()
	if p2.all_cards==[]:
		print("Player 1 WINS!")
		exit()

def card_draw(l):

	p1_card=p1.remove_one()
	print("Player 1 put",p1_card)
	p2_card=p2.remove_one()
	print("Player 2 put",p2_card)

	win()

	l.extend([p1_card,p2_card])

	if p1_card.value>p2_card.value:
		print("Player 1 won this round")
		p1.add_cards(l)
		print(p1,p2)
		l=[]
		win()
		
	if p1_card.value<p2_card.value:
		print("Player 2 won this round")
		p2.add_cards(l)
		print(p1,p2)
		l=[]
		win()

	if p1_card.value==p2_card.value:
		time.sleep(3)
		print("WAR")
		card_draw(l)

	time.sleep(3)

print("YOU are Player 1")
p1=Player("1")
p2=Player("2")

deck=Deck()
deck.shuffle()
for i in range(26):
	p1.add_cards(deck.deal_one())
	p2.add_cards(deck.deal_one())

print(p1)
print(p2)

game_on,war=True,True
tries=0

while game_on:

	tries+=1

	if tries>=50:
		p1.shuffle()
		p2.shuffle()

	l=[]

	card_draw(l)