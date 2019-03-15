class Character:

	def __init__(self, full_name, gender, species, home_planet, lifespan, movies_list):
		self.full_name = full_name
		self.gender = gender
		self.species = species
		self.home_planet = home_planet
		self.lifespan = lifespan
		self.movies_list = movies_list

	def get_character_name(self):
		return self.full_name

	def get_gender(self):
		return self.gender

	def get_species(self):
		return self.species

	def get_home_planet(self):
		return self.home_planet

	def get_lifespan(self):
		return self.lifespan

	def get_movies_list(self):
		return self.movies_list

	def set_species(self, species_link_updated):
		self.species = species_link_updated

	def set_home_planet(self, homeplanet_updated):
		self.home_planet = homeplanet_updated

	def set_lifespan(self, lifespan_updated):
		self.lifespan = lifespan_updated

	def set_movies_list(self, movies_list_updated):
		self.movies_list = movies_list_updated