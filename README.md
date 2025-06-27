# AI-interviewer-bot

## structure
ai-interviewer-chatbot/
├── frontend/                  # React or HTML/JS interface
│   ├── public/
│   └── src/
│       ├── components/       # Chat UI, Input Box, Feedback Panel
│       └── App.js
├── backend/                  # API logic
│   ├── routes/               # /ask, /score, etc.
│   └── app.py (or index.js)  # FastAPI / Node.js
├── prompts/                  # YAML/JSON files for LLM prompts
│   ├── hr_prompt.txt
│   ├── tech_prompt.txt
│   └── stress_prompt.txt
├── scoring/                  # Response evaluation logic
│   └── rubric.py
├── feedback/                 # Logic to generate feedback summaries
│   └── feedback_generator.py
├── llm_integration/          # Wrapper for OpenAI / Claude
│   └── llm_call.py
├── .env                      # API keys, environment vars
├── README.md
└── requirements.txt / package.json
