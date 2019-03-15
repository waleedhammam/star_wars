'''
' ## API endpoint returns character data via POST Request
' 	with payload data of a dictionary with the name of
' 	the requested character
' 	data={"name":"--your requested character name--"}
' 	return result will be a json object with a key of
' 	character index and value of his data
' 	could be multiple characters in same request upon the name
' 
' ## index_html endpoint returns a html template to deal with
'	it via html, it renders a template with searchbox
'''

from flask import Flask, request, json, render_template
from character import Character
import requests, json, os, sys

# starting Flask app
try:
	app = Flask(__name__)
except KeyboardInterrupt:
	print("^C pressed, Server is shutting down")

# Loading configurations from config.json file
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

# API endpoint
@app.route('/api', methods=['GET', 'POST'])
def api():
	all_data = {}
	if request.method == 'POST':
		payload = {'search': request.form['name']}
		seach_result = search(people_api_url, payload)
		characters_needed_data = optmize_results(seach_result)

		if characters_needed_data == "404":
			return "404 Not found", 404
		final_chars = render_linked_results(characters_needed_data)

		for i in range(len(final_chars)):
			all_data.update({ i : vars(final_chars[i]) })

	response = app.response_class(
		response=json.dumps(all_data),
		status=200,
		mimetype='application/json'
	)
	print(json.dumps(all_data, indent=4))
	return response

@app.route('/', methods=['GET', 'POST'])
def index_html():
	all_data = {}
	if request.method == 'POST':
		payload = {'search': request.form['name']}
		seach_result = search(people_api_url, payload)
		characters_needed_data = optmize_results(seach_result)

		if characters_needed_data == "404":
			return "404 Not found", 404
		final_chars = render_linked_results(characters_needed_data)

		for i in range(len(final_chars)):
			all_data.update({ i : vars(final_chars[i]) })
	return render_template('index.html', data=all_data)

# Helper functions
# Search 
def search(search_key, *args):
	if search_key == people_api_url:
		search_request = requests.get(api_base_url + people_api_url, params=args[0])
	else:
		search_request = requests.get(search_key)
	return search_request.json()

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
		return "404"

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
	app.run(host=host_ip, port=host_port)