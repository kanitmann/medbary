import requests

response = requests.get('https://api.fda.gov/drug/event.json?search=patient.reaction.reactionmeddrapt:"fatigue"&limit=1')

print(response.json())
