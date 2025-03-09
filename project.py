import os
import requests
import google.generativeai as gai
import gradio as gr
import markdown


from groq import Groq
from dotenv import load_dotenv
from bs4 import BeautifulSoup



class Gemini_gradio:
    def __init__(self):
        load_dotenv()
        self.groq_api = os.getenv("GROQ_API_KEY")
        self.google_api = os.getenv("GOOGLE_API_KEY")
        gai.configure(api_key=self.google_api, transport="rest")
        groq_ai = Groq(api_key=self.groq_api)

        self.system_message = "You are a helpful assistant and you are trained by Ankith Reddy Subhanpuram not Google"


    def message_google(self, prompt):
        gemini = gai.GenerativeModel(
            model_name='gemini-2.0-flash-exp',
            system_instruction=self.system_message
        )

        # response = gemini.generate_content(prompt)
        # html_content = markdown.markdown(response.text)

        # soup = BeautifulSoup(html_content,"html.parser")

        # return soup.get_text()  

        text = ""
        response_stream = gemini.generate_content(prompt,stream=True)  # Streaming response
        for response in response_stream:
            if response.text:
                text += response.text
                yield text





if __name__ == "__main__":
    model_init = Gemini_gradio()
    #response = model_init.message_google("What do you think about my friend kalyan")
    gr.Interface(fn=model_init.message_google,inputs=[gr.Textbox(label="Enter your Prompt")], outputs=[gr.Markdown(label="Response")],allow_flagging="never").launch(share=True)