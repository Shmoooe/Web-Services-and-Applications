import mysql.connector
from mysql.connector import pooling
from spotify_config import config

def create_database():
    cnx = mysql.connector.connect(
        host=config["db_host"],
        user=config["db_user"],
        password=config["db_pass"]
    )
    cur= cnx.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {config['db_name']}")
    cur.close()
    cnx.close()

create_database()

pool = pooling.MySQLConnectionPool(
    pool_name= "mypool",
    pool_size= 5,
    host= config["db_host"],
    user= config["db_user"],
    password= config["db_pass"],
    database= config["db_name"],
    autocommit= True
)

def get_conn():
    return pool.get_connection()

def init_tables():
    query= """
    CREATE TABLE IF NOT EXISTS artists(
        id          INT             PRIMARY KEY AUTO_INCREMENT,
        name        VARCHAR(80)     NOT NULL,
        genre       VARCHAR(120),
        popularity  INT,
        spotify_id  VARCHAR(100)    UNIQUE
    );
    """
    with get_conn() as cnx, cnx.cursor() as cur: 
        cur.execute(query)

def all_artists():
    with get_conn() as cnx, cnx.cursor(dictionary=True) as cur:
        cur.execute("SELECT * FROM artists")
        return cur.fetchall()
    
def find_by_id(artist_id):
    with get_conn() as cnx, cnx.cursor(dictionary=True) as cur:
        cur.execute("SELECT * FROM artists WHERE id = %s", (artist_id,))
        return cur.fetchone()
    
def insert_artist(name, genre, popularity, spotify_id):
    query = """
    INSERT INTO artists (name, genre, popularity, spotify_id)
    VALUES (%s, %s, %s, %s)
    """
    with get_conn() as cnx, cnx.cursor() as cur:
        cur.execute(query, (name, genre, popularity, spotify_id))
        return cur.lastrowid
    
def delete_artist(artist_id):
    with get_conn() as cnx, cnx.cursor() as cur:
        cur.execute("DELETE FROM artists WHERE id=%s", (artist_id,))
        return cur.rowcount