import gradio as gr
import json
from swarm_editor import SwarmEditor
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

load_dotenv()

CONFIG_FILE = 'swarm_config.json'

class UserInterface:
    def __init__(self):
        self.swarm_editor = SwarmEditor()
        self.firecrawl_app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        self.load_config()

    def load_config(self):
        with open(CONFIG_FILE, 'r') as f:
            self.config = json.load(f)
        self.swarm_editor.load_configuration(CONFIG_FILE)
        return self.config

    def scrape_website(self, url):
        scrape_status = self.firecrawl_app.scrape_url(
            url,
            params={'formats': ['markdown']}
        )
        return scrape_status.get('markdown', 'No content scraped')

    def update_agent(self, index, name, instructions):
        self.swarm_editor.update_agent(index, name, instructions)
        return f"Agent {index} updated"

    def run_workflow(self, scraped_content):
        response = self.swarm_editor.run_workflow(scraped_content)
        return response.messages[-1]["content"]

    def launch(self):
        with gr.Blocks() as interface:
            gr.Markdown("# Swarm Editor with Firecrawl")
            
            url = gr.Textbox(label="URL to Scrape", value="https://www.okgo.app/")
            scrape_button = gr.Button("Scrape Website")
            scraped_content = gr.Textbox(label="Scraped Content")
            
            agent_tabs = gr.Tabs()
            
            with agent_tabs:
                for i, agent in enumerate(self.config['agents']):
                    with gr.Tab(f"Agent {i}"):
                        name = gr.Textbox(label="Name", value=agent['name'])
                        instructions = gr.Textbox(label="Instructions", value=agent['instructions'], lines=3)
                        update_button = gr.Button(f"Update Agent {i}")
                        update_output = gr.Textbox(label="Update Status")
                        update_button.click(self.update_agent, inputs=[gr.Number(value=i, visible=False), name, instructions], outputs=[update_output])
            
            run_button = gr.Button("Run Workflow")
            workflow_output = gr.Textbox(label="Workflow Output")

            scrape_button.click(self.scrape_website, inputs=[url], outputs=[scraped_content])
            run_button.click(self.run_workflow, inputs=[scraped_content], outputs=[workflow_output])

        interface.launch()

if __name__ == "__main__":
    ui = UserInterface()
    ui.launch()