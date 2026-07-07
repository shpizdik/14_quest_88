
class Item:
	def __init__ (self, name, weight):
		self.name = name
		self.weight = weight

class Inventory:
	def __init__ (self, max_weight):
		self.items = [] 
		self.max_weight = max_weight 
	

	def add_item(self, item):
		if sum(i.weight for i in items) + item.weight <= max_weight:
			self.items.append(item)
			return True
		else:
			return False

	def drop_item(self, item):
		if item in self.items:
			self.items.remove(item)
			return True
		else:
			return False

class Player:
	def __init__ (self, health, oxygen, max_carriage, inventory):
		self.health = health
		self.oxygen = oxygen
		self.max_carriage = max_carriage
		self.inventory = Inventory(self.max_carriage)

	def turn_left(self): pass
	
	def turn_right(self): pass

	def move_forward(self): pass

	def masturbate(self): pass

class Ebaka: pass

class Space: pass

class Corridor: pass


