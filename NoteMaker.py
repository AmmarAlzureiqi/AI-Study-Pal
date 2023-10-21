import os
import openai
import streamlit as st
st.title('NoteMaker Program')

openai.api_key = "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"

# notes = input("NOTES TO SUMMARIZE:")
# # notes = "Structural Differences in Distinct Classes of Cells Thus far we have been describing the structure and function of eukaryotic animal cells. As we have mentioned earlier, there are different classes of cells. In this short section, we will discuss the major cellular differences between prokaryotic and eukaryotic cells, and between animal and plant cells. The diversity among various cells is a result of the varying functions and complexity of those cells. Because plants convert sunlight into energy rather than obtaining energy by eating food the way we humans do, plant cells require additional structures that can perform this function. While most structures between animal and plant cells are the same, there are a couple of additional structures that perform specific functions in plant cells that are unnecessary in animal cells. In contrast to eukaryote cells, prokaryotic cells lack membrane-bound organelles. Such organization is necessary in eukaryotic cells because eukaryotes are often multi-cellular organisms whose cells communicate with the help of specific membrane-bound structures. Because prokaryotic cells do not form such complex networks, a single compartment containing all of the essential biomolecules for life is sufficient. We will begin our discussion by contrasting plant and animal cells and then move on to the structural differences between prokaryotic and eukaryotic cells."

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "YOU ARE A NOTE SUMMARIZING ASSISTANT"},
#     {"role": "user", "content": f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {notes} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES, AND CREATE 3-5 STUDY QUESTIONS"}
#   ]
# )

# print(completion['choices'][0]['message']['content'])

user_input = st.text_input("Enter some text:")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "YOU ARE A NOTE SUMMARIZING ASSISTANT"},
    {"role": "user", "content": f"CAN YOU GIVE ME A SUMMARY OF THESE NOTES {user_input} THAT IS 33% THE LENGTH OF THE ORIGINAL NOTES, AND CREATE 3-5 STUDY QUESTIONS"}
  ]
)


st.write("You sumamarized notes:", completion)


