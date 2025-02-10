
from crewai.flow.flow import Flow, start, listen, router
from litellm import completion


API_KEY =" "

class RoutedFlow(Flow):
    
    @start()
    def generate_topic(self):
        response = completion(
            model = 'gemini/gemini-2.0-flash-lite-preview-02-05',
            api_key = API_KEY,
            messages=[{"role": "user", "content": "Generate a blog topic for 2030."}]
        )
        topic = response["choices"][0]["message"]["content"].strip()
        # For demonstration, add a fake flag to the state.
        self.state["is_tech"] = "tech" in topic.lower()
        print(f"Topic: {topic}")
        return topic

    @router(generate_topic)
    def route_topic(self):
        # Route based on the is_tech flag.
        if self.state.get("is_tech"):
            return "tech_route"
        else:
            return "lifestyle_route"

    @listen("tech_route")
    def generate_tech_outline(self, topic):
        response = completion(
            model = 'gemini/gemini-2.0-flash',
            api_key = API_KEY,
            messages=[{"role": "user", "content": f"Create a detailed tech blog outline for: {topic}"}]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print("Tech Outline:")
        print(outline)
        return outline

    @listen("lifestyle_route")
    def generate_lifestyle_outline(self, topic):
        response = completion(
            model = 'gemini/gemini-2.0-flash-lite-preview-02-05',
            api_key = API_KEY,
            messages=[{"role": "user", "content": f"Create a detailed lifestyle blog outline for: {topic}"}]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print("Lifestyle Outline:")
        print(outline)
        return outline

#if __name__ == "__main__":

def kickoff():
    
    flow = RoutedFlow()
    final_output = flow.kickoff()
    print("Final Output:")
    print(final_output)
