class Computer:
	def __init__(self, processor, ram, storage, graphic_card):
		self.processor = processor
		self.ram = ram
		self.storage = storage
		self.graphic_card = graphic_card
    
  	def configuration(self):
		return {
			'processor':self.processor,
			'ram':self.ram,
			'graphic_card': self.graphic_card,
			'storage':self.storage,
		}
	

	class Laptop(Computer):
		def __init__(self, processor, ram, stroage, graphic_card):
			self.super(processor, ram, storage, graphic_card)
			
		
