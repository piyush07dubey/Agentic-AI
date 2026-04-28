import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
# Make sure to import GroqLLM, for example:
# from src.langgraphagenticai.llms import GroqLLM 

def load_langgraph_agentic_app():
    """
    Loads the Langgraph Agentic AI application.
    """
    ui_obj = LoadStreamlitUI()

    # FIX 1: Added parentheses assuming this is a method returning a dictionary. 
    # If it is an attribute/property, remove the ().
    user_input = ui_obj.load_streamlit_ui() 

    # FIX 2: Corrected indentation so this is inside the function
    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return 

    # FIX 3: Moved the usecase check here so it validates before processing chat
    usecase = user_input.get("selected_usecase")
    if not usecase:
        st.error("No use case selected")
        return  # FIXED: Removed the extra space that was causing an IndentationError here

    # FIX 4: Corrected indentation for the chat input
    user_message = st.chat_input("Enter your message:")
    
    if user_message:
        # FIX 5: Indented the try block and added the missing except block
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: Failed to load the LLM model.")
                return 
                
            # Add your logic here to handle the user_message with the model
            # st.write(f"Processing: {user_message}")

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            return 