# import streamlit as st
# from PIL import Image
# import time
# from llm import Chatbot  # Assuming your Chatbot class is in a file named chatbot.py

# # Set page config
# st.set_page_config(
#     page_title="Appointment Scheduler",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Apply dark theme
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #1E1E1E;
#         color: #FFFFFF;
#     }
#     .stTextInput > div > div > input {
#         background-color: #2E2E2E;
#         color: #FFFFFF;
#     }
#     .stButton > button {
#         background-color: #4CAF50;
#         color: #FFFFFF;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Load images
# bot_image = Image.open("bot_image.jpg")  # Replace with your robot image path
# user_image = Image.open("user_image.webp")  # Replace with your user image path

# # Initialize session state
# if 'bot' not in st.session_state:
#     st.session_state.bot = Chatbot()
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# # Title
# st.title("🤖 Appointment Scheduler")

# # Chat interface
# chat_container = st.container()

# # User input
# user_input = st.text_input("Type your message here...")

# if st.button("Send"):
#     if user_input:
#         # Add user message to chat history
#         st.session_state.chat_history.append(("user", user_input))
        
#         # Get bot response
#         bot_response = st.session_state.bot.process_input(user_input)
        
#         # Add bot response to chat history
#         st.session_state.chat_history.append(("bot", bot_response))

# # Display chat history
# with chat_container:
#     for role, message in st.session_state.chat_history:
#         col1, col2 = st.columns([1, 9])
        
#         with col1:
#             if role == "user":
#                 st.image(user_image, width=50)
#             else:
#                 st.image(bot_image, width=50)
        
#         with col2:
#             if role == "user":
#                 st.text_area("You:", value=message, height=100, key=f"user_{time.time()}", disabled=True)
#             else:
#                 st.text_area("Bot:", value=message, height=100, key=f"bot_{time.time()}", disabled=True)

# # Add some spacing at the bottom
# st.markdown("<br><br>", unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# st.markdown("© 2024 Appointment Scheduler. All rights reserved.")

# import streamlit as st
# from llm import Chatbot  # Import your Chatbot class

# def main():
#     st.title("Appointment Booking Chatbot")

#     # Initialize session state
#     if 'chatbot' not in st.session_state:
#         st.session_state.chatbot = Chatbot()
#     if 'messages' not in st.session_state:
#         st.session_state.messages = []

#     # Display chat messages
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Chat input
#     if prompt := st.chat_input("Type your message here..."):
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Get chatbot response
#         response = st.session_state.chatbot.process_input(prompt)

#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": response})
#         with st.chat_message("assistant"):
#             st.markdown(response)

# if __name__ == "__main__":
#     main()

import streamlit as st
from llm import Chatbot  # Import your Chatbot class

EXIT_PHRASES = ['exit', 'quit', 'bye', 'thank', 'no thank you', "that's all"]

def main():
    st.title("Appointment Booking Chatbot")

    # Initialize session state
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = Chatbot()
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'conversation_ended' not in st.session_state:
        st.session_state.conversation_ended = False

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if not st.session_state.conversation_ended:
        if prompt := st.chat_input("Type your message here..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Check for exit phrases
            if any(phrase in prompt.lower() for phrase in EXIT_PHRASES):
                response = "Thank you for using our service. Goodbye!"
                st.session_state.conversation_ended = True
            else:
                # Get chatbot response
                response = st.session_state.chatbot.process_input(prompt)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

            # Rerun the app to update the UI
            st.rerun()
    else:
        st.write("The conversation has ended. Refresh the page to start a new conversation.")

if __name__ == "__main__":
    main()