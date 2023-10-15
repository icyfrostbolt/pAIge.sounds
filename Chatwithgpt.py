import os
import openai

#openai.api_key = os.getenv("OPENAI_API_KEY2")  # API key
openai.api_key = "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"

def chat_with_gpt(book_name):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "make a playlist of 3 songs with just song titles and " +
                                              "artists that match the vibe of " +
                                              book_name +
                                              "in json format named playlist, organized with \'title\' and artist" +
                                              ". Only include JSON in your response " +
                                              "with no other words"}],
        max_tokens=1024)
    content = (response.choices[0].message.content)
    #print(content)
    return content

chat_with_gpt("Twilight")