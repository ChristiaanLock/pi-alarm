import http.client, urllib.parse # Importeer alle nodige modules
from time import time
import json

class Telegram(): # Initialiseer Klasse Telegram

	apiKey = "bot299779325:AAG2zQb823R7L5QtQAGUZJTe6fRE_9c8kvU" # Definieer de API sleutel
	api = "api.telegram.org" # Defineer de API host

	def doRequest(self, apiMethod, data): # Defineer de methode doRequest waar alle api request naar telegram gebruik van maken
		params = urllib.parse.urlencode(data) # Encodeer de data zodat deze als POST data kan worden gebruikt
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"} # Defineer de HTTP headers
		conn = http.client.HTTPSConnection(self.api) # Begin de connectie met de API!
		conn.request("POST", "/" + self.apiKey + "/" + apiMethod, params, headers) # Doe een request, met de API key en API methode
		response = conn.getresponse() # Haal het resultaat op
		return [response.status, response.reason, response.read().decode('utf-8')] # Geef het resultaat terug, samen met de HTTP status en reden

	def sendMessage(self, msg, username): # Stuur een telegram bericht naar een gebruiker
		self.doRequest("sendMessage", {'chat_id': username, 'text': msg}) # do de request

	
