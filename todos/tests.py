import sys

from todos.models import User_Category, Todo

import  requests,pprint



response = requests.get('http://localhost:8000/todos/list_todo')

pprint.pprint(response.json())