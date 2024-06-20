import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

with open('index.json', 'w') as index:
    index.write(response.text)

# fdsfdsfds


# sdfsdfsdf


# sdffsdfsdfsd

# fsdfsdfsdf



# fsdfsd




# with open('data.json', 'w') as json_file:
#     json_file.write("""{
#     "data": 123 
# }""")