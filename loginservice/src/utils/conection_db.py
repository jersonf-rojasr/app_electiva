import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
config = {
  'user': os.getenv('USERDB'),
  'password': os.getenv('PASSWORD'),
  'host': os.getenv('HOSTDB'),
  'database': os.getenv('DATABASE')
}

condb = mysql.connector.connect(**config)
