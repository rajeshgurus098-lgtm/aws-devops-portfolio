from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="food-db",
        user="root",
        password="password123",
        database="fooddb"
    )

@app.route("/")
def home():
    return "Welcome to Rajesh's Food Delivery App!"

@app.route("/menu")
def get_menu():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
