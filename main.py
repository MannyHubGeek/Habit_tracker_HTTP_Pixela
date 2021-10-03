import datetime

import requests
import datetime
from datetime import timedelta
USERNAME = "mannyboy"
TOKEN = "8yihnejqi02jjkejoa"
GRAPH_ID = "manny-graph"
QUANTITY = "10"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "8yihnejqi02jjkejoa",
    "username": "mannyboy",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN":TOKEN
}

tempdatenow = datetime.date.today()
tempyesterdaydate = datetime.date.today() - timedelta(1)
datenow = str(tempdatenow).replace('-','')
yest = str(tempyesterdaydate).replace('-','')
#yesterdate = datetime.datetime.strptime(str(tempyesterdaydate), "%yyyy%m%d")
print(datenow)
print(yest)

graph_params = {
"id":"manny-graph",
 "name":"coding-days",
 "unit":"commit",
 "type":"int",
 "color":"shibafu",
 # "timezone":"Asia/Tokyo",
 # "isSecret":"true",
 # "publishOptionalData":"true"
}

# Create a Graph
response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

# pixela_endpoint_user = "https://pixe.la/@mannyboy"
# mydetails = requests.get(url=pixela_endpoint_user)

# Post a Pixel  #####################################################################################

pixel_params = {
    "id":GRAPH_ID,
    "date": datenow,
    "quantity": QUANTITY,
    "name": "coding-days",
    "unit": "Github Commit",
    "type": "int",
    "color": "momiji"

}
# Create a PIXEL #####################################################################################

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

#####################################################################################

################################ Put a pixel i.e modify a already existing value ######################################

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

#####################################################################################

########################## delete a pixel i.e delete an already existing value ###################################

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yest}"
response = requests.delete(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)



