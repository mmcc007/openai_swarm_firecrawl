# Swarm Firecrawl Marketing Agent

A multi-agent system using [OpenAI Swarm](https://github.com/openai/swarm) for AI-powered marketing strategies using [Firecrawl](https://firecrawl.dev) for web scraping. Now featuring a Gradio-based user interface for easy interaction.

## Agents

1. User Interface: Manages user interactions
2. Website Scraper: Extracts clean LLM-ready content via Firecrawl API
3. Analyst: Provides marketing insights
4. Campaign Idea: Generates marketing campaign concepts
5. Copywriter: Creates compelling marketing copy

## Requirements

- [Firecrawl](https://firecrawl.dev) API key
- [OpenAI](https://platform.openai.com/api-keys) API key
- Python 3.7+

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

### Command-Line Interface

Run the main script to start the interactive CLI demo:

```
python main.py
```

### Gradio User Interface

To use the Gradio-based user interface:

```
python gradio_ui.py
```

This will launch a local web server. Open the provided URL in your web browser to interact with the Swarm Firecrawl Marketing Agent through a user-friendly interface.

## Features

- Web scraping using Firecrawl API
- Multi-agent system for comprehensive marketing analysis
- Interactive command-line interface
- Gradio-based graphical user interface
- Real-time updates on scraping and agent progress

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.