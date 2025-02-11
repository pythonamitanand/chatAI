from flask import Flask, render_template, request, jsonify
from datetime import datetime
from datetime import date
import random
import re

app = Flask(__name__)

class chatAIJsonData:
    def __init__(self):
        self.easy_patterns = {
            r'hi|hello|hey': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! How are you doing?"
            ],
             r'good morning|good evenig|good night': [
                "You too....[AMIT]?"
            ],
            r'how are you': [
                "I'm doing well, thanks for asking! How about you?",
                "I'm great! What can I help you with today?"
            ],
            r'python': [
                "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected.",
                "Python is a high-level, interpreted programming language known for its simplicity and readability."
            ],
            r'azure': [
                "Microsoft Azure is a cloud computing platform and service offered by Microsoft. It provides a wide range of cloud services, including computing, storage, networking, databases, artificial intelligence, and more.",
                "Azure More.."
            ],
             r'html': [
                "we will add content for html soon...."
            ],
            

        }
        
        self.responses = {
            r'weather|temperature': [
                "I don't have access to real-time weather data, but I can help you find a weather service!",
                "Would you like to know about weather patterns in general?"
            ],
            r'time': [
                f"The current time is {datetime.now().strftime('%H:%M')}",
                "Is there something specific about time you'd like to know?"
            ],
             r'what is time': [
                f"The current time is {datetime.now().strftime('%H:%M')}",
                "Is there something specific about time you'd like to know?"
            ],
            r'date': [
                f"The current date is {date.today()}",
                "Is there something specific about time you'd like to know?"
            ],
            r'name': [
                "I'm WebBot, nice to meet you!",
                "You can call me WebBot. How can I assist you?"
            ],
            r'help': [
                "I can help with basic conversations, tell you the time, or just chat!",
                "I'm here to help! We can talk about various topics or I can assist with simple tasks."
            ]
        }
        
        self.fallback_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more about that.",
            "I'm still learning. Could you elaborate?",
            "That's a good question. Could you provide more details?"
        ]
    
    def get_response(self, user_data):
        """Generate a response based on user input"""
        processed_request = user_data.lower().strip()
        
        # Check for greetings first
        for pattern, responses in self.easy_patterns.items():
            if re.search(pattern, processed_request):
                return random.choice(responses)
        
        # Check for other patterns
        for pattern, responses in self.responses.items():
            if re.search(pattern, processed_request):
                return random.choice(responses)
        
        # If no pattern matches, use fallback
        return random.choice(self.fallback_responses)

# Created bot instance for getting message
chatAI = chatAIJsonData()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message_data = request.json['message']
    chatAI_response = chatAI.get_response(user_message_data)
    return jsonify({
        'response': chatAI_response,
        'timestamp': datetime.now().strftime('%H:%M')
    })

if __name__ == '__main__':
    app.run(debug=True)