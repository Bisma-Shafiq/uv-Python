from crewai.flow.flow import Flow, listen, start
import time

class sampleflow(Flow):

    @start()
    def fun1(self):
        print("step1")
        time.sleep(2)

    @listen(fun1)
    def fun2(self):
        print("step2")  
        time.sleep(2)
    
    @listen(fun2)
    def fun3(self):
        print("step3")
        time.sleep(2)

def kickoff():
    sim = sampleflow()
    sim.kickoff()