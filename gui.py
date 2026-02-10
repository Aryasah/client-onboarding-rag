import streamlit as st

class AssistantGUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.messages = assistant.messages
        self.employee_information = assistant.employee_information
    
    def render_messages(self):
        messages = self.messages
        for message in messages:
            if message["role"] == "ai":
                st.chat_message("assistant").markdown(message["content"])
            else:
                st.chat_message("human").markdown(message["content"])

    def get_response(self, user_input):
        return self.assistant.get_response(user_input)

    def set_state(self, key, value):
        st.session_state[key] = value

    def render_user_input(self):
        user_input = st.chat_input("Type here ...", key="input")
        if user_input and user_input.strip() != "":
            st.chat_message("human").markdown(user_input)
            # 
            response = self.get_response(user_input)
            st.chat_message("assistant").markdown(response)

            self.messages.append({"role": "user", "content": user_input})
            self.messages.append({"role": "ai", "content": response})

            self.set_state("messages", self.messages)

    def render(self):
        with st.sidebar:
            st.logo("https://upload.wikimedia.org/wikipedia/commons/0/0e/Umbrella_Corporation_logo.svg")
            st.title("Umbrella Corp Onboarding Assistant")
            st.subheader("Employee Information")
            st.write(self.employee_information)
        
        self.render_messages()

        self.render_user_input()