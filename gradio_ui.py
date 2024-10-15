import gradio as gr
from main import user_interface_agent, scrape_website, analyze_website_content, create_campaign_idea, generate_copy
from swarm import Swarm, Agent, Response
from typing import Dict, Any

class GradioSwarmApp:
    def __init__(self):
        self.client = Swarm()
        self.messages = []
        self.agent = user_interface_agent
        self.context_variables = {}

    def process_message(self, message: str) -> Dict[str, Any]:
        self.messages.append({"role": "user", "content": message})
        response = self.client.run(
            agent=self.agent,
            messages=self.messages,
            context_variables=self.context_variables,
            stream=False
        )
        self.messages.extend(response.messages)
        self.agent = response.agent
        self.context_variables.update(response.context_variables)
        return self.format_response(response)

    def format_response(self, response: Response) -> Dict[str, Any]:
        formatted_response = {
            "assistant_message": "",
            "scraper_output": "",
            "agent_outputs": []
        }
        
        for message in response.messages:
            if message["role"] == "assistant":
                formatted_response["assistant_message"] += f"{message['sender']}: {message['content']}\n"
            elif message["role"] == "tool":
                if message["tool_name"] == "scrape_website":
                    formatted_response["scraper_output"] = message["content"]
                else:
                    formatted_response["agent_outputs"].append(f"{message['tool_name']}:\n{message['content']}")
        
        return formatted_response

def create_ui():
    app = GradioSwarmApp()
    
    with gr.Blocks() as interface:
        gr.Markdown("# Swarm Firecrawl Marketing Agent")
        
        with gr.Row():
            input_text = gr.Textbox(label="Enter URL or message")
            submit_btn = gr.Button("Submit")
        
        with gr.Row():
            assistant_output = gr.Textbox(label="Assistant Output", lines=10)
        
        with gr.Row():
            scraper_output = gr.Textbox(label="Scraper Output", lines=10)
            agent_outputs = gr.Textbox(label="Agent Outputs", lines=10)
        
        def process_input(message):
            response = app.process_message(message)
            return (
                response["assistant_message"],
                response["scraper_output"],
                "\n\n".join(response["agent_outputs"])
            )
        
        submit_btn.click(
            process_input,
            inputs=[input_text],
            outputs=[assistant_output, scraper_output, agent_outputs]
        )
    
    return interface

if __name__ == "__main__":
    ui = create_ui()
    ui.launch()