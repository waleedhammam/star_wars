#############
## testcase #
#############
# api link: https://swapi.co/api/
# endpoint: people/1
# response:	{
				"name": "Luke Skywalker",
				"height": "172",
				"mass": "77",
				"hair_color": "blond",
				"skin_color": "fair",
				"eye_color": "blue",
				"birth_year": "19BBY",
				"gender": "male",
				"homeworld": "https://swapi.co/api/planets/1/",
				"films": [
					"https://swapi.co/api/films/2/",
					.
					.
				],
				"species": [
					"https://swapi.co/api/species/1/"
				.
				.
			}
# endpoint: films/2/
# response: {
				"title": "The Empire Strikes Back",
				"episode_id": 5,
				"opening_crawl": "It is a dark time for 
				.
				.
			}
# endpoint: species/1/
# response: {
				"name": "Human",
				"classification": "mammal",
				"designation": "sentient",
				"average_lifespan": "120",
				.
				.
			}
	
# endpoint: planets/1/
# response: {
				"name": "Tatooine",
				"rotation_period": "23",
				"orbital_period": "304",
				"diameter": "10465",
				"climate": "arid",
				.
				.
			}
#####################
# Required Results  #
#####################
{
    "0": {
        "movies_list": [
            "The Empire Strikes Back",
            "Revenge of the Sith",
            "Return of the Jedi",
            "A New Hope",
            "The Force Awakens"
        ],
        "home_planet": "Tatooine",
        "gender": "male",
        "species": "Human",
        "full_name": "Luke Skywalker",
        "lifespan": "120"
    }
}
######## END #########