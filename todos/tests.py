import sys

from todos.models import Todo

import  requests,pprint



response = requests.get('http://localhost:8000/todos/list_todo')

pprint.pprint(response.json())