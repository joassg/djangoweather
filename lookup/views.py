from django.shortcuts import render

# Create your views here.

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']		
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=ECB9B09D-6F00-4120-9A54-DF2599A90D88")
	 
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error ..."

		if api[0]['Category']['Name'] == "Good":
			category_color = "good"
			category_description = "(0 to 50)	Air quality is considered satisfactory, and air pollution poses little or no risk."
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 to 100)	Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "USG":
			category_description = "(101 to 150)	Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 to 200)	Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealty"
		elif api[0]['Category']['Name'] == "Very Unhealty":
			category_description = "(201 to 300)	Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 to 500)	Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"

		return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color} )

	else:
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=ECB9B09D-6F00-4120-9A54-DF2599A90D88')
	 
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error ..."

		if api[0]['Category']['Name'] == "Good":
			category_color = "good"
			category_description = "(0 to 50)	Air quality is considered satisfactory, and air pollution poses little or no risk."
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 to 100)	Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "USG":
			category_description = "(101 to 150)	Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 to 200)	Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealty"
		elif api[0]['Category']['Name'] == "Very Unhealty":
			category_description = "(201 to 300)	Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 to 500)	Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"

		return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color} )


def about(request):
	return render(request, 'about.html', {})
