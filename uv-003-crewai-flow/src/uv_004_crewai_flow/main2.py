from crewai.flow.flow import Flow, listen, router, start

import random
import time

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Hello! I am a bot, I can help you with some tasks.")
    
    @router(greeting)
    def select_country(self):
        country = ['india','pakistan','usa','china','japan']
        select_country = random.choice(country)
        print(select_country)
        return select_country
    @listen(select_country)
    def india(self,country):
        print(f"Famous food of given {country}.")
        time.sleep(2)
    @listen(select_country)
    def pakistan(self,country):
        print(f"Famous food of given {country}.")
        time.sleep(2)
    @listen(select_country)
    def usa(self,country):
        print(f"Famous food of given {country}.")
        time.sleep(2)
    @listen(select_country)
    def china(self,country):
        print(f"Famous food of given {country}.")
        time.sleep(2)
    @listen(select_country)
    def japan(self,country):
        print(f"Famous food of given {country}.")
        time.sleep(2)

def kickoff():
    obj = RouteFlow()
    obj.kickoff()

def plot():
    obj = RouteFlow()
    obj.plot()
    