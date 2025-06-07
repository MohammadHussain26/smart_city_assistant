import gradio as gr
from model import generate_response

def respond(prompt):
    return generate_response(f"As a smart city assistant, answer: {prompt}")

gr.Interface(fn=respond,
             inputs="text",
             outputs="text",
             title="Sustainable Smart City Assistant",
             description="Ask about traffic, water usage, waste, or air quality.").launch()
