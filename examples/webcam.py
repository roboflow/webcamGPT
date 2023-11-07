import gradio as gr
import numpy as np

import webcamgpt

connector = webcamgpt.OpanAIConnector()


def respond(image: np.ndarray, prompt: str, chat_history):
    response = connector.simple_prompt(image=image, prompt=prompt)
    chat_history.append((prompt, response))
    return "", chat_history


with gr.Blocks() as demo:
    with gr.Row():
        webcam = gr.Image(source="webcam", streaming=True)
        with gr.Column():
            chatbot = gr.Chatbot()
            message = gr.Textbox()
            clear_button = gr.ClearButton([message, chatbot])

    message.submit(respond, [webcam, message, chatbot], [message, chatbot])

demo.launch(debug=False, show_error=True)