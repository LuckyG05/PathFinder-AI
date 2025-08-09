# PathFinder-AI
PathFinder AI is a personalized AI-powered study companion. It helps users master any subject through a structured and interactive approach.

---

##  Project Overview
PathFinder AI is an interactive command-line application that acts as a personal tutor, guiding students through a structured learning journey for any subject. By leveraging the power of AI, it creates a custom learning roadmap, provides detailed notes, conducts interactive quizzes, and tracks progress. The goal is to make self-learning more organized, effective, and engaging.

---

## Features
* **Personalized Roadmap Generation:**  Enter any subject, and the AI will generate a step-by-step learning roadmap tailored for you.

* **Tutoring:**  Get comprehensive notes on each topic and ask clarifying questions before taking a mini-quiz.

* **Dynamic Quizzing:**  The AI generates unique questions for each session to ensure a fresh learning experience.

* **Progress Tracking:**  Monitor your progress to see which topics you've completed and which are still remaining.

* **Final Test:**  Take a comprehensive multiple-choice test on all completed topics to assess your mastery of the subject.

---

## Getting Started
### Prerequisites
Before you can run this project, you need to have the following installed:

* Python 3.6 or higher

* An OpenAI API Key

### Installation
1. Clone the repository:
```bash
git clone https://github.com/LuckyG05/PathFinder-AI.git
```
```bash
cd PathFinder-AI
```

2. Install the required libraries:

```bash
pip install openai
````
3. Set up your OpenAI API Key:
You need to set your API key as an environment variable.

```bash
set OPENAI_API_KEY=your_api_key_here
``` 

---

## How to Use
1. Run the application from your terminal:
```bash
python pathfinder_ai.py
```
2. Enter a subject you want to learn (e.g., Python, Calculus, History).

3. Choose a topic number from the generated roadmap to start your tutoring session.

4. Within a session, you can:

* Type a question to get more details from the AI.

* Type test to begin a quiz on the topic.

* Type quit to end the session.

5. From the main menu, you can also type P to check your progress or test to take a final test on all completed topics.

---

## Built With
* **Python:**  The core programming language used for the application logic.

* **OpenAI API:**  Powers the AI's ability to generate content, questions, and notes.

---

## Future Scope
Given more time, I would like to expand PathFinder AI with the following features:

* Web Interface: Transition from a command-line interface to a user-friendly web application using a framework like Flask.

* User Data Persistence: Implement a simple database (e.g., SQLite) to save user progress across different sessions.

* Advanced Personalization: Allow users to choose their learning style or set specific goals to further tailor the AI's responses.

---

## Contact
If you have any questions or feedback, feel free to reach out:
* **GitHub:** [LuckyG05](https://github.com/LuckyG05)

---
