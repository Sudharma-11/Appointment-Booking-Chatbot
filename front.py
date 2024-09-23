import streamlit as st
from llm import Chatbot  # Import your Chatbot class

EXIT_PHRASES = ['exit', 'quit', 'bye', 'thank', 'no thank you', "that's all"]

def main():
    st.title("📅 Appointment Booking Chatbot")
    
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
