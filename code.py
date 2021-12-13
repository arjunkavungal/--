response = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + text_input.replace(" ","+")+ "&key=AIzaSyCYKIKheo-kxVkwr8Aq3468SbhIfXm_-C4&country=US")
response_json = response.json()
items = response_json['items']
prices(items)
