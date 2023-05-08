import psycopg2
from psycopg2.extras import RealDictCursor
import json

conn = psycopg2.connect(database='postgres', host='127.0.0.1', password='postgres', user='postgres')
cur = conn.cursor(cursor_factory=RealDictCursor)

