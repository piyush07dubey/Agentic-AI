from src.langgraphagenticai.LLMS.groqllm import GroqLLM
import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.display_result import DisplayResultStreamlit
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

    user_message=st.chat_input("Enter youre message:")
    if user_message:
        try:
          obj_llm_config=GroqLLM(user_controls_input=user_input)
          model=obj_llm_config.get_llm_model()
          
          if not model:
                        st.error("Error:LLM could not initilized")
                        return

                        usecase=user_input.get("selected_usecase")
                        if not usecase:
                            st.error("Error:Usecase could not be selected")
                            return
                        
          graph_builder=GraphBuilder(model)
          try:
            graph=graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
          except Exception as e:
                st.error(f"Error:Graph could not be initilized{e}")
                return
          
                       
            
        except Exception as e:
            st.error("error")

