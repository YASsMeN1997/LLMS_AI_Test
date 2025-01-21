from utils.helper_functions import *
from assets import *
import gradio as gr
import os

# Create the Gradio interface
def main():
    with gr.Blocks() as demo:
        gr.Markdown("### Car Information Submission")
        
        # Textbox for car description input
        description_input = gr.Textbox(label="Car Description", placeholder="Enter the car description here...", lines=4)
        
        # Image upload input
        image_input = gr.Image(type="filepath", label="Upload Car Image")
        
        # Textbox for email input
        email_input = gr.Textbox(label="Your Email", placeholder="Enter your email", type="email")
        
        # Button to submit the data and process the car information
        submit_button = gr.Button("Send Car Details")
        
        # Output message area
        output_message = gr.Textbox(label="Output", interactive=False)
        
        # Set the button to call the process_car_info function on click
        submit_button.click(process_car_info, inputs=[description_input, image_input, email_input], outputs=output_message)
    
    # Launch the Gradio app
    demo.launch()

main()

