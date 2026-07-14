import psycopg
import os
import requests

from dotenv import load_dotenv
load_dotenv()

def get_data(city):
    api_url=f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q={city}&aqi=no"
    try:
        response=requests.get(api_url)
        if response.status_code==200:
            print("Data fetched successfully")
            raw_data=response.json()
            return raw_data
        else:
            print(f"Failed : {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Failed to fetch data{e}")
        return None

def transform_data(raw_data):
    data={
        "city":raw_data["location"]["name"],
        "temp":raw_data["current"]["temp_c"],
        "humidity":raw_data["current"]["humidity"],
        "description":raw_data["current"]["condition"]["text"]
    }
    return data


def connect_db():
        
    try:
        connection=psycopg.connect(
                    host=os.getenv("host"),
                    port=os.getenv("port"),
                    dbname=os.getenv("database"),
                    user=os.getenv("user"),
                    password=os.getenv("password")
        )
        return connection
    except psycopg.Error as e:
        print(f"failed connection {e}")
        return None


def insert_record(connection,data):
    city=data["city"]
    temp=data["temp"]
    humid=data["humidity"]
    desc=data["description"]
    query="INSERT INTO weather_data(City,temperature,humidity,weather_desc) VALUES (%s,%s,%s,%s);"
    cursor=connection.cursor()
    cursor.execute(query,(city,temp,humid,desc))
    connection.commit()
    cursor.close()


def main():
    city=input("Enter the city name:")
    raw_data=get_data(city)
    if raw_data:
        data=transform_data(raw_data)
        connection=connect_db()
        if connection:
            print("connection successful")
            try:
                insert_record(connection,data)
            except psycopg.Error as e:
                print(f"Insertion failed{e}")
            connection.close()
            print("connection closed")

main()