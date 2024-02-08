from email.policy import EmailPolicy
import requests
from email_send import send_email

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
  "X-RapidAPI-Key": "e15fc80b6amshfb1da622649a231p107513jsn90c9cd535978",
  "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

final_joke = response.json()

joke = final_joke["body"][0]["setup"] + " " + final_joke["body"][0]["punchline"]

email = input("Enter recipient's email: ")
sender_email = 'joshuasmallnyc@gmail.com'
sender_password = 'szyt jerp dvlv virw'
subject = 'Dad Joke of the Day'

send_email(sender_email, sender_password, email, subject, joke)