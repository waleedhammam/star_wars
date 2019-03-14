from flask import Flask, request, jsonify, render_template
from character import Character
import requests, json, os, sys

# Flask app
app = Flask(__name__)

# Configurations
CURRENT_ROOT = os.path.abspath(os.path.dirname(__file__))
config_file_path = os.path.join(CURRENT_ROOT, 'config.json')
with open(config_file_path) as json_data_file:
	config_data = json.load(json_data_file)

# config host
host = config_data['host']
host_ip = host['host_ip']
host_port = host['host_port']

# config APIs
apis_data = config_data['apis']
api_base_url = apis_data['base_url']
people_api_url = apis_data['people_url']

@app.route('/api', methods=['GET', 'POST'])
def api():
	all_data = {}
	if request.method == 'POST':
		payload = {'search': request.form['name']}
		seach_result = search(people_api_url, payload)

		characters_needed_data = optmize_results(seach_result)
		final_chars = render_linked_results(characters_needed_data)

		for i in range(len(final_chars)):
			all_data.update({ i : vars(final_chars[i]) })
			
	print(json.dumps(all_data, indent=4))
	return json.dumps(all_data, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index_html():
	all_data = {}
	if request.method == 'POST':
		payload = {'search': request.form['name']}
		seach_result = search(people_api_url, payload)

		characters_needed_data = optmize_results(seach_result)
		final_chars = render_linked_results(characters_needed_data)

		for i in range(len(final_chars)):
			all_data.update({ i : vars(final_chars[i]) })
			
	print(json.dumps(all_data, indent=4))
	return render_template('index.html', data=all_data)
	

# Search 
def search(search_key, *args):
	if search_key == people_api_url:
		search_request = requests.get(api_base_url + people_api_url, params=args[0])
	else:
		search_request = requests.get(search_key)
	return search_request.json()

# Helper functions
# Optmize results accoring to needs, removing unncesccary ones
def optmize_results(search_data):
	characters = []
	people_count = search_data['count']
	people_details = search_data['results']
	if people_count > 0:
		for i in range(people_count):
			name = people_details[i]['name']
			gender = people_details[i]['gender']
			species = people_details[i]['species'][0]
			lifespan = people_details[i]['species'][0]
			home_planet = people_details[i]['homeworld']
			movies = people_details[i]['films']
			characters.append(Character(name, gender, species, home_planet, lifespan, movies))
		return characters
	else:
		return {}

# replacing urls with its data
def render_linked_results(characters):  
	for avatar in characters:
		avatar.set_species(get_species_by_url(avatar.get_species()))
		avatar.set_home_planet(get_home_planet_by_url(avatar.get_home_planet()))
		avatar.set_lifespan(get_lifespan_by_url(avatar.get_lifespan()))
		avatar.set_movies_list(get_movie_title_by_url(avatar.get_movies_list()))
	return characters

# rendering homeplanet name via url to its destination api
def get_home_planet_by_url(home_planet_url):
	homeplanet_details = search(home_planet_url)
	return homeplanet_details['name']

# rendering species name via url to its destination api
def get_species_by_url(species_url):
	species_details = search(species_url)
	return species_details['name']

# rendering lifespan via url to its destination api
def get_lifespan_by_url(lifespan_url):
	lifespan_details = search(lifespan_url)
	return lifespan_details['average_lifespan']

# rendering movies names via url to its destination api
def get_movie_title_by_url(movie_urls):
	movie_details = []
	for movie_url in movie_urls:
		movie_title = search(movie_url)
		movie_details.append(movie_title['title'])
	return movie_details


if __name__ == "__main__":
	app.run(host=host_ip, port=host_port, threaded=False, debug=True)