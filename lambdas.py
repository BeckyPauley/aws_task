########################## Exercise 1 ##########################

import json

# Section 1 and 2:

def lambda_handler(event, context):
# "Hello world!" string acessed in event data 
    print(event['key1'])
    return event['key1']

# Section 4: simplified function to focus on API 

def lambda_handler(event, context):
    print("Hello World!")
    return "Hello World!"

# Section 5: pass a query parameter of “name”. If name, return "Hello <name>!" else return "Hello World!"

def lambda_handler(event, context):
    if len(event['name']) > 0:
        return "Hello {}!".format(event['name'])
    return "Hello World!"

# Mapping template:
{
  "name" : "$input.params('name')"
}