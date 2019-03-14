# star_wars
flask app that exposes API which takes the name of a character as input and returns its information

### endpoints
`/` html template returns data in text form <br />
`/api` json return type 

### Post request
on the end point `/api` with the payload `data={"name":"--your requested character name--"}` , this will return result in json form

### Application requirments:
- python3
- pip3

### Installation process:
1- clone the repo:
`git clone https://github.com/waleedhammam/star_wars.git`

2- dive in the directory of star_wars and run:
`pip3 install -r requirments.txt`

(**note** you maybe need to do `sudo` for the third step if you are running on linux)

(**note** there's also `dockerfile` in `docker` directory for instant deployment)

### Running the application:
run the server with
`python3 server.py`
