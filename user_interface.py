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

    def update_agent(self, index, name, prompt):
        self.swarm_editor.update_agent(index, name, prompt)
        return f"Agent {index} updated"

    def run_workflow(self, scraped_content, progress=gr.Progress()):
        outputs = [""] * len(self.swarm_editor.agents)
        for i, agent in enumerate(self.swarm_editor.agents):
            progress(i / len(self.swarm_editor.agents), f"Running Agent {i}: {agent.name}")
            response = self.swarm_editor.run_single_agent(agent, scraped_content)
            outputs[i] = response.messages[-1]['content']
            scraped_content = outputs[i]
            yield outputs
        progress(1.0, "Workflow complete")

    def launch(self):
        with gr.Blocks() as interface:
            gr.Markdown("# Agent Workflow Editor")
            
            url = gr.Textbox(label="URL to Scrape", value="https://www.lazzloe.com/")
            scrape_button = gr.Button("Scrape Website")
            scraped_content = gr.Textbox(label="Scraped Content")
            
            agent_config_tabs = gr.Tabs()
            with agent_config_tabs:
                for i, agent in enumerate(self.config['agents']):
                    with gr.Tab(f"Agent {i} Config"):
                        name = gr.Textbox(label="Name", value=agent['name'])
                        prompt = gr.Textbox(label="Prompt", value=agent['instructions'], lines=3)
                        update_button = gr.Button(f"Update Agent {i}")
                        update_output = gr.Textbox(label="Update Status")
                        update_button.click(self.update_agent, inputs=[gr.Number(value=i, visible=False), name, prompt], outputs=[update_output])
            
            run_button = gr.Button("Run Workflow")
            
            output_tabs = gr.Tabs()
            output_components = []
            with output_tabs:
                for i, agent in enumerate(self.config['agents']):
                    with gr.Tab(f"Agent {i} Output"):
                        output = gr.Textbox(label=f"{agent['name']} Output", lines=10)
                        output_components.append(output)

            scrape_button.click(self.scrape_website, inputs=[url], outputs=[scraped_content])
            run_button.click(
                self.run_workflow,
                inputs=[scraped_content],
                outputs=output_components
            )

        interface.launch()

if __name__ == "__main__":
    ui = UserInterface()
    ui.launch()