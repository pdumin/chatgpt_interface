import openai
import streamlit as st
from streamlit_chat import message

# for local run 
# from key import key


# for streamlit run
openai.api_key = st.secret['key']

def generate_response(prompt):
    completion=openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.6,
    )

    message=completion.choices[0].text
    return message

st.title("")

# temperature = st.slider('Temp', min_value=0.0001, max_value=2., step=.1)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input=st.text_input(" ",key='input')

if user_input:
    output=generate_response(user_input)

    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')