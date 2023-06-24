import streamlit as st
from streamlit_chat import message
from bardapi import Bard


def generate_response(prompt):
    token = 'xxxxxx'
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']

    return response


def get_text():
    input_text = st.text_input("ENTER THE TEXT BELOW:", "", key='input')
    return input_text


# Title of the streamlit app
# st.title('AI CHAT BOT!')
st.markdown('<h1 style="color: #0707e3;">AI CHAT BOT!</h1>', unsafe_allow_html=True)


changes = '''
<style>
[data-testid = "stAppViewContainer"]{
        background-color: #e5e5f7;
        opacity: 0.8;
        background-image: radial-gradient(circle at center center, #dbc9c2, #e5e5f7), repeating-radial-gradient(circle at center center, #dbc9c2, #dbc9c2, 10px, transparent 20px, transparent 10px);
        background-blend-mode: multiply;
    }
 [data-testid = "stMarkdownContainer"]{
 color:#e3071d
 }  
 [data-testid = "stHeader"]{
 background-color:rgba(0,0,0,0)
 }    

</style>
'''

st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

# Accepting the input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):

        message(st.session_state['past'][i], key="key_"+str(i),is_user=True)
        message(st.session_state['generated'][i], key=str(i))


