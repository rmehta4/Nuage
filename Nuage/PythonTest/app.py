import json
import sys
from urllib2 import urlopen
import requests
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


logger = logging.getLogger()
handler = logging.FileHandler('todoApp.log')
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)



def get_option():
  try:
    opt = raw_input("Please enter the number: ")
  except ValueError:
    logger.error("invalid input " , opt)
    print("Oops! That was no valid number.Try again...")
    
  return opt


def get_request():
  url = "http://152.46.20.242:80/api/todos"
  logger.info("sending GET request to %s" , str(url))
  response = requests.get(url)
  data = response.json()
  logger.info("Received GET data %s" , str(data))
  return data['result']
 
def read_todos():
  dict1 = dict()
  jsonData = get_request()
  print ("\n**************  To-do list *************")
  count = 1
  for todo in jsonData:
     print str(count),'.',str(todo['task'])
     dict2 = {}
     dict2[todo['task']] = todo['_id']
     dict1[count] = dict2
     count = count + 1
  print ("**************************************")
  return dict1

def delete_todos():
  dict1 = read_todos()
  for key, value in dict1.iteritems():
     print key,value.items()[0][0]
  var = raw_input("Please enter todo to delete: ")
  for key, value in dict1.iteritems():
     if int(key) == int(var):
       _id = value.items()[0][1]
  url = "http://152.46.20.242:80/api/todos/" + _id
  logger.info("sending DELETE request to %s" , str(url))
  response = requests.delete(url)
  read_todos()
  return
 
def post_todos():
  task = raw_input("Please enter a task for the to-do list : ")
  url = "http://152.46.20.242:80/api/todos"
  logger.info("sending POST request to %s" , str(url))
  r = requests.post(url, json={"text": str(task)})
  read_todos()


def select_options():
  print "Please select one of the following options"
  print "1) get list of Todos"
  print "2) create new todo"
  print "3) delete todo"
  print "4) exit"
  opt = get_option()
  if int(opt) == 1:
     read_todos()
     select_options()
  elif int(opt) == 2:
     post_todos()
     select_options()
  elif int(opt) == 3:
     delete_todos()
     select_options()
  elif int(opt) == 4:
     print ("Exiting from the to-do list")
     sys.exit(1)

select_options()
  

