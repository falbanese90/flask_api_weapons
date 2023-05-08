from db import conn, cur
import json

class WeaponsStore():
    def index():
        cur.execute('SELECT * FROM weapons;')
        result = cur.fetchall()
        return json.dumps(result, indent=2)
    
    def add_weapon(name, points):
        sql = 'INSERT INTO WEAPONS (name, points) VALUES (%s, %s) RETURNING *;'
        cur.execute(sql, (name, points))
        result = cur.fetchone()
        return json.dumps(result, indent=2)
