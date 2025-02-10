import os 
from litellm import completion

os.environ["GOOGLE_API_KEY"]= os.getenv("GOOGLE_API_KEY")
def call_gemini():
    response=completion(
        model='gemini/gemini-1.5-flash',
        messages=[
            {"role": "system", "content": "Hello, how are you?"}
        ]
    )
    print(response['choices'][0]['message']['content'])
    