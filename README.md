# chatAI
Created ChatAI bot using python and html

# Python AI Chatbot with Web Interface

A simple, extensible chatbot application with a modern web interface built using Python, Flask, and vanilla JavaScript.

## Features

### Core Functionality
- Pattern-based response generation
- Real-time chat interface
- Time-aware responses
- Contextual conversation handling
- Fallback responses for unknown queries

### Web Interface
- Clean, modern UI design
- Mobile-responsive layout
- Real-time message updates
- Message history with timestamps
- Support for both click and Enter key interactions

## Installation

### Prerequisites
- Python 3.7+
- Flask

### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/pythonamitanand/chatAI
cd chatAI
```


3. Install required packages:
```bash
pip install flask
```

4. Create the project structure:
```
chatAI/
├── app.py
├── README.md
└── templates/
    └── index.html
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Start chatting with the bot!

## Customization

you can setup on your local and do some magic 



## Project Structure

### Backend (`app.py`)
- Flask server setup
- chatAIJsonData class implementation
- Route handlers for chat functionality
- Response generation logic

### Frontend (`index.html`)
- Responsive web interface
- Real-time message handling
- Message display formatting
- User input processing


### Common Issues

1. Server won't start:
   - Check if port 5000 is available
   - Verify Flask installation
   - Ensure Python version compatibility

2. Messages not sending:
   - Check browser console for errors
   - Verify network connectivity
   - Ensure JavaScript is enabled

## API Reference

### Endpoints

#### POST /chat
Handles chat messages and returns bot responses.

Request body:
```json
{
    "message": "user message here"
}
```

Response:
```json
{
    "response": "bot response here",
    "timestamp": "HH:MM"
}
```




## Acknowledgments

- Flask web framework
- Modern web development best practices
- Pattern matching techniques for chatbots

## Contact

For questions and support, please open an issue in the repository or contact the maintainers.