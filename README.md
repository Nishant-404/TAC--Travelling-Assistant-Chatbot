📍 TAC - Travel Assistant Chatbot
TAC (Travel Assistant Chatbot) is an AI-powered travel suggestion web application that helps users find personalized travel destinations based on their interests. 
It offers smart recommendations for places, hotels, and transport, along with attractive image previews.
Built with Flask and integrated with Groq's LLaMA 3, Pexels, and a secure login system, TAC simulates an intelligent travel planner accessible via a chatbot interface.

🔍 Features
✅ AI Chatbot powered by Groq's LLaMA 3
🏖️ Suggests destinations based on user intent (e.g., "I want a beach trip within 300 km")
🏨 Hotel recommendations for long trips
🚗 Transport suggestions (mode & time) for long-distance travel
🖼️ Destination image previews using Pexels API
💬 Natural language input supported (typos and slang handled)
🔐 Login & Register system with SQLite backend
🕓 Session persistence with session timeout
💡 Dynamic UI with modern travel-themed styling
📄 Chat history viewing + CSV export
🌗 Light/Dark mode toggle



📁 Folder Structure
TAC-Travel-Assistant/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── travel_bg.jpg (optional)
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── chat.html
│   └── history.html
│
├── main.py
├── database.db
├── requirements.txt
└── README.md


⚙️ Technologies Used
| Stack    | Tech                  |
| -------- | --------------------- |
| Backend  | Python, Flask         |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite                |
| AI Chat  | Groq (LLaMA 3)        |
| Images   | Pexels API            |




🔑 API Keys Required
To run the project successfully, you need:
| API                | Description                     | Required for          |
| ------------------ | ------------------------------- | --------------------- |
| **Groq API Key**   | For accessing LLaMA 3 model     | AI travel suggestions |
| **Pexels API Key** | For fetching destination images | Image previews        |



📍 Where to insert API keys:
Open main.py and replace:
GROQ_API_KEY = 'your_groq_api_key_here'
PEXELS_API_KEY = 'your_pexels_api_key_here'



🛠️ Installation & Setup
1. Clone the Repository   
git clone https://github.com/your-username/tac-travel-assistant.git
cd tac-travel-assistant

2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Flask App
python main.py



✍️ How to Use
1.Open in browser → http://localhost:5000
2.Register / Login with a username
3.Start chatting using natural prompts like:
  "Suggest a mountain trip from Delhi"
  "I want to go on a solo 3-day bike trip"
4.View place images and info right in the chat
5.Export your chat history if needed


🧩 Future Enhancements (Ideas)
React-based frontend with real-time typing animation
Google Maps integration for live travel time
Multi-language support (e.g., Hindi, Spanish)
Voice-based input
User preference learning & personalization


✅ To-Do for User
Before deployment or full use:
Replace placeholder API keys in main.py
Customize background images in static/images/
Set debug=False for production (main.py)
Optionally update branding/logo in HTML templates


