from swarm_editor import SwarmEditor
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

load_dotenv()

def scrape_website(url):
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        raise ValueError("FIRECRAWL_API_KEY environment variable not set")
    
    app = FirecrawlApp(api_key=api_key)
    scrape_status = app.scrape_url(
        url,
        params={'formats': ['markdown']}
    )
    return scrape_status.get('markdown', 'No content scraped')

def integration_test():
    # Create SwarmEditor instance
    editor = SwarmEditor()

    # Load configuration from JSON file
    editor.load_configuration('swarm_config.json')

    # Scrape the website using Firecrawl
    url = "https://www.okgo.app/"
    scraped_content = scrape_website(url)

    # Run the workflow with scraped content as initial input
    response = editor.run_workflow(scraped_content)

    # Output the result of the final agent to stdout
    print("Final output:")
    print(response.messages[-1]["content"])

if __name__ == "__main__":
    integration_test()