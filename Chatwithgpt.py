import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY2")  # API key

def chat_with_gpt(book_name):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "make a playlist of 20 songs with just song titles and " +
                                              "artists that match the vibe of " +
                                              book_name +
                                              "in json format"}],
        max_tokens=1024)
    content = (response.choices[0].message.content)
    print(content)



chat_with_gpt("Twilight")