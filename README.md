# Swarm Firecrawl Marketing Agent

A multi-agent system using OpenAI's Swarm for AI-powered content analysis and generation, integrated with Firecrawl for web scraping. This project features a Gradio-based user interface for easy interaction and configuration of the agent swarm.

## Features

- Web scraping using Firecrawl API
- Configurable multi-agent system for content analysis and generation
- Interactive Gradio-based graphical user interface
- Real-time updates on scraping and agent progress
- Ability to modify agent configurations on-the-fly

## Requirements

- Python 3.7+
- Firecrawl API key
- OpenAI API key

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/swarm-firecrawl-marketing-agent.git
   cd swarm-firecrawl-marketing-agent
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   FIRECRAWL_API_KEY=your_firecrawl_api_key
   ```

## Usage

### User Interface

To use the Gradio-based user interface:

1. Run the user interface:
   ```
   python user_interface.py
   ```

2. In the Gradio interface:
   - The URL is pre-filled with https://www.okgo.app/, but you can change it if needed.
   - Click "Scrape Website" to fetch the content.
   - Modify agent configurations in the respective tabs if desired.
   - Click "Run Workflow" to process the scraped content through the SwarmEditor.

### Configuration

The system uses a configuration file to define the agents in the swarm. You can modify the `swarm_config.json` file to change the number of agents, their names, and instructions.

Example configuration:
```json
{
  "agents": [
    {
      "name": "Agent 1",
      "instructions": "Process the input data and provide initial insights."
    },
    {
      "name": "Agent 2",
      "instructions": "Analyze the insights from Agent 1 and generate recommendations."
    },
    {
      "name": "Agent 3",
      "instructions": "Create a final report based on the recommendations from Agent 2."
    }
  ]
}
```

### Integration Test

To run the integration test:

```
python integration_test.py
```

This will use Firecrawl to scrape https://www.okgo.app/, then pass the scraped content through the SwarmEditor workflow, and finally output the result to stdout.

## Project Structure

- `swarm_editor.py`: Contains the SwarmEditor class for managing the agent swarm.
- `user_interface.py`: Implements the Gradio-based user interface.
- `integration_test.py`: Provides an end-to-end test of the system.
- `swarm_config.json`: Configuration file for defining the agent swarm.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.