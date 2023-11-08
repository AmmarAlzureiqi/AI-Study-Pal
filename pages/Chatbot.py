import openai
import streamlit as st

openai.api_key = st.secrets["API_KEY"]

def createChat(subject = 'biology'):
    tempstring = f"You are a {subject} expert"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": tempstring},
    ]
    )

    generated_text = response['choices'][0]['message']['content'] #response.choices[0].text.strip()
    return generated_text


st.title("Your Personal Study Expert")
topic = st.text_area("Enter Study Subject: Whatever subject you enter here, your study bot will become an expert in!", 
                     value= 'ie. Biology', height=50)

tempoutput = createChat(subject = topic)
st.write(tempoutput)








# openai.api_key = 

# messages = []
# system_msg = input("What type of chatbot would you like to create?\n")
# messages.append({"role": "system", "content": system_msg})

# print("Your new assistant is ready!")
# while input != "quit()":
#     message = input()
#     messages.append({"role": "user", "content": message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\n" + reply + "\n")


