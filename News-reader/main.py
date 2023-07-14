import requests
import json
import time

def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch("SAPI.spVoice")
      speak.Speak(str)

if __name__ == '__main__':
      
      print("*********  Welcome to our news channel  *********")
      speak("Welcome to our news channel")
      print("    Listen Headlines of your interested topics   ")
      speak("Listen Headlines of your interested topics")
      topics = ''' 1.Buisness \n 2.Technology \n 3.Sports \n 4.Science \n 5.Health \n 6.Entertainment'''
      print(topics)
      print("------- Press respective numbers for specific topics ------")
      tpn = int(input("Enter the topic you are interested in : "))

      try:
            if tpn==1  :     
                  print("Top Buisness Headlines are :")
                  speak("Top Buisness Headlines are :")
                  url = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=565124840a8a44c9bbd3a64b65560ead"
            elif tpn==2 :     
                  print("Top Technology Headlines are :")
                  speak("Top Technology Headlines are :")
                  url = f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=565124840a8a44c9bbd3a64b65560ead"
            elif tpn==3 :     
                  print("Top Sports Headlines are :")
                  speak("Top Sports Headlines are :")
                  url = f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=565124840a8a44c9bbd3a64b65560ead"
            
            elif tpn==4 :     
                  print("Top Science Headlines are :")
                  speak("Top Science Headlines are :")
                  url = f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=565124840a8a44c9bbd3a64b65560ead"
            elif tpn==5 :     
                  print("Top Health Headlines are :")
                  speak("Top Health Headlines are :")
                  url = f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=565124840a8a44c9bbd3a64b65560ead"
            elif tpn==6 :     
                  print("Top Entertainment Headlines are :")
                  speak("Top Entertainment Headlines are :")
                  url = f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=565124840a8a44c9bbd3a64b65560ead"
            else:
                  print("Invalid Choice.Please choose from given options above!")      
                  speak("Invalid Choice.") 
            
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for i in range(1,11):
                  for articles in arts:
                        print(f"{i}--{articles['title']}")
                        speak(articles['title'])
                        print("----> To get full description , Open this link :", articles['url'],"\n")
                        i+=1
                        if i>=11:
                              break
                        if i==10:
                              speak("The last news is")
                        else:
                              speak("Moving on to the next news..Listen Carefully")
                        

      except Exception as e:
            print("Try again")

print("Thanks for visiting our channel !")
speak("Thanks for visiting our channel !")
      






                        
      



