import json

def readProfiles():
	with open('profiles.json') as f:
		myStr = f.read()
		myObj = json.loads(myStr)
		return myObj['profiles']

PROFILES = []
for p in readProfiles():
	if 'number' in p:
		if 'profile' in p:
			PROFILES.append(p)

# profiles_list = set([x['profile'] for x in PROFILES])

BEER_PROFILES = {
	'Practitioner': 'Bock',
	'Undershift': 'Industrial Lager',
	'Result': 'India Pale Ale', # Result Oriented
	'Specialist': 'Winter Ale',
	'Achiever': 'Imperial India Pale Ale',
	'Persuader': 'Amber Ale',
	'Creative': 'NEIPA',
	'Tight': 'Industrial Lager', 
	'Counselor': 'Weizen',
	'Objective Thinker': 'Pale Ale',
	'Developer': 'Stout',
	'Agent': 'Saison',
	'Investigator': 'Historical Beer',
	'Inspirational': 'Any Style',
	'Perfectionist': 'Old Ale',
	'Promoter': 'Speciality Beer',
	'Overshift': 'Industrial Lager',
	'Appraiser': 'Barley Wine'
}

"""
profs = readProfiles() 
search = [1, 3, 2, 1]
for prof in profs:
	if prof['number'] == 1321:
		print(prof)
"""