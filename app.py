from flask import Flask
import mariadb

app = Flask(__name__)
conn = mariadb.connect(
         host='192.168.0.176',
         port= 3306,
         user='user6',
         password='1',
         database='bisp')
cur = conn.cursor()
@app.route("/index")
def index():
    return "Connected to database"
if __name__ == "__main__":
    app.run()
