import random


class Card:

  suit = 'none'
  value = 'none'

  def __init__(self,suit,value):
    self.suit = suit
    self.value = value
	
class Deck:
  
  stack = [] # Empty array to hold the deck
  
  def __init__(self):
    self.restack()

  def shuffle(self):  
    random.shuffle(self.stack)
	
  def restack(self):
  
    self.stack[:] = [] # Empty deck
	
    suits = ['H','S','D','C']
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    for suit in suits:
      for value in values:
        self.stack.append(Card(suit,value))
		
  def pull(self):
    return self.stack.pop()
	
class Solitaire:
  
  deck = Deck()
  table = []
  
  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle() # Shuffle deck

  def solve(self):
    
    self.table.append(self.deck.pull())
    #print(self.table[-1].suit,self.table[-1].value)
	
    for x in xrange(len(self.deck.stack)):
      self.table.append(self.deck.pull())
      #print(self.table[-1].suit,self.table[-1].value)

      found = False

      if (len(self.table) >= 2):
        if(self.table[-1].value == self.table[-2].value):
          found = True
          self.table[-2:-1] = []
      if ( ( not found ) and (len(self.table) >= 3)):
        if(self.table[-1].value == self.table[-3].value):
		  found = True
		  self.table[-3:-1] = []
      if ( ( not found ) and (len(self.table) >= 4)):
        if(self.table[-1].value == self.table[-4].value):
		  found = True
		  self.table[-4:-1] = []
	  
    return len(self.table)

  def reset(self):
    self.deck.restack()
    self.deck.shuffle()
    self.table[:] = []
	  
	    
	