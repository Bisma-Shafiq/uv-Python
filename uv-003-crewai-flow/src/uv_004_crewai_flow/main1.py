from crewai.flow.flow import Flow, listen, start
import time
from litellm import completion


API_KEY =" "

class cityfunfact(Flow):

    @start()
    def generate_city_name(self):
        result = completion(
            model = 'gemini/gemini-2.0-flash-lite-preview-02-05',
            api_key = API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": "Generate random city name in the Indonesia.",
                },
            ],
        )

        random_city = result['choices'][0]['message']['content']
        print(random_city)
        return random_city
    
    @listen(generate_city_name)
    def fun_fact_generation(self,random_city):
        result = completion(
            model = 'gemini/gemini-2.0-flash-thinking-exp-01-21',
            api_key = API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}.",
                },
            ],
        )

        fun_fact = result['choices'][0]['message']['content']
        print(fun_fact)
        self.state['fun_fact']=fun_fact

    @listen(fun_fact_generation)
    def save_fun_fact(self):
        with open('fun_fact.md','w') as file:
            file.write(self.state['fun_fact'])
            return self.state['fun_fact']


def kickoff():
    sim = cityfunfact()
    result = sim.kickoff()
    print(result)
    
