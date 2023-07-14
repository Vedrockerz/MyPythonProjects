import requests
import json


def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch("SAPI.spVoice")
      speak.Speak(str)

if __name__ == '__main__':
      a = int(input("enter 1 or 2"))
      i=1

      if a==1 :
            speak("Top Buisness Headlines are as follows")
            url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=565124840a8a44c9bbd3a64b65560ead"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for articles in arts:
                  # for i in range(1,11):
                  print(f"{articles['title']}")
                  speak(articles['title'])

      if a==2 :
            speak("Top sports Headlines are as follows")
            url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=565124840a8a44c9bbd3a64b65560ead"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for articles in arts:
                  # for i in range(1,11):
                  print(f"{articles['title']}")
                  speak(articles['title'])

while True:
      if i>=2:
            break
      i+=1
           
           
                  