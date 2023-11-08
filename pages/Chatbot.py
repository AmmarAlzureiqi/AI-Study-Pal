import openai
import streamlit as st

st.title("Your Personal Study Expert")
st.subheader(openai.__version__)

st.subheader("Whatever subject you enter here, your study bot will become an expert in!")
topic = st.text_area("Enter Study Subject: (Feel free to add what grade or year of study you are in as well)")


openai.api_key = st.secrets["API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

    

if topic:
    initialprompt = f"Hello, I'd like to focus on {topic} and have you assist me in studying this field comprehensively. Please provide detailed explanations, summaries, and answer questions on various {topic} topics. Additionally,if I ask for clarification or further examples, kindly provide those as well. Let's delve deep into the world of {topic} to help me improve my understanding and knowledge in this subject."
    st.session_state.messages.append({"role": "assistant", "content": initialprompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Begin Chatting!"):
    st.session_state.messages.append({"role": "assistant", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# import openai
# import streamlit as st
# from openai import OpenAI



# st.title("Your Personal Study Expert")

# st.subheader("Whatever subject you enter here, your study bot will become an expert in!")
# topic = st.text_area("Enter Study Subject: (Feel free to add what grade or year of study you are in as well)")


# openai.api_key = st.secrets["API_KEY"]

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if topic:
#     initialprompt = f"Hello, ChatGPT. I'd like to focus on {topic} and have you assist me in studying this field comprehensively. Please provide detailed explanations, summaries, and answer questions on various {topic} topics. Additionally,if I ask for clarification or further examples, kindly provide those as well. Let's delve deep into the world of {topic} to help me improve my understanding and knowledge in this subject."
#     st.session_state.messages.append({"role": "assistant", "content": initialprompt})

# for message in st.session_state.messages:
#     if message["role"] == "assistant" and message["content"] == initialprompt:
#         continue
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("Begin Chatting!"):
#     st.session_state.messages.append({"role": "assistant", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         for response in OpenAI().chat.completion.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         ):
#             full_response += response.choices[0].delta.get("content", "")
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})










