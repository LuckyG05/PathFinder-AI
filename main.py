import openai
import os
from openai import OpenAI
import time

# Initialize global variables for the API client and user progress
client = None
user_progress = {}

def get_openai_response(prompt_text):
    """
    Sends a prompt to the OpenAI API and returns the response.
    This function handles all communication with the AI.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt_text}
            ],
            max_tokens=500,
            temperature=0.5
        )
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content.strip()
        else:
            return "An error occurred: The API response was empty or malformed."
    except Exception as e:
        return f"An error occurred: {e}"

def generate_roadmap(subject):
    """
    Generates a step-by-step learning roadmap for a given subject.
    """
    prompt = f"""
    Create a simple, step-by-step learning roadmap for a high school student to master the subject: '{subject}'.
    Break it down into 5-7 main topics with a brief description for each.
    Present the roadmap as a numbered list.
    """
    print("Generating your personalized roadmap...")
    return get_openai_response(prompt)

def conduct_tutoring_session(topic):
    """
    Starts an interactive Q&A session on a chosen topic.
    Includes detailed notes and a mini-quiz.
    """
    print("\n--- Tutoring Session Started ---")
    print(f"Let's learn about: {topic}")
    
    notes_prompt = f"Provide a detailed and comprehensive explanation of the topic: '{topic}' for a new learner. Include definitions, key concepts, and simple, relevant examples. Structure the explanation with headings and bullet points for clarity."
    notes = get_openai_response(notes_prompt)
    print("\n--- Notes ---")
    print(notes)
    
    user_progress[topic] = "in-progress"
    
    print("\nDo you have any questions about this topic, or should we move on to a quick test? Type your question, or type 'test' to begin the quiz.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'test':
            break
        elif user_input.lower() == 'quit':
            print("Bot: Okay, session ended. This topic remains 'in-progress'.")
            return
        
        doubt_prompt = f"The user asked: '{user_input}'. Please provide a clear and concise answer related to the topic '{topic}'."
        doubt_answer = get_openai_response(doubt_prompt)
        print(f"Bot: {doubt_answer}")
        print("\nDo you have any more questions, or should we move on to the test? Type your question, or type 'test' to begin.")
        
    print("\nNow, let's test your knowledge with a few questions. Type 'quit' to end this session anytime.")
    
    questions_count = 0
    asked_questions = [] # Store asked questions here
    
    while questions_count < 3: # We'll ask 3 questions
        # Modified prompt: tell the AI which questions were already asked
        prompt_question = f"You are a tutor. Ask a new, different, and unique question about the topic '{topic}'. Do not ask any of these questions: {', '.join(asked_questions)}. Keep it basic, easy, short and one liner."
        
        question = get_openai_response(prompt_question)
        print(f"\nBot (Tutor): {question}")
        
        # Add the new question to our list
        asked_questions.append(question)
        
        user_answer = input("Your Answer: ")
        
        if user_answer.lower() == 'quit':
            break
        
        prompt_evaluation = f"The user's answer to the question '{question}' was: '{user_answer}'. Is this answer correct? If not, provide the correct answer and a brief explanation. Keep the response concise."
        evaluation = get_openai_response(prompt_evaluation)
        print(f"Bot (Tutor): {evaluation}")
        questions_count += 1
        time.sleep(1)

    if questions_count >= 2: # Topic is marked complete if at least 2 questions are answered
        print("\nBot: You've completed a few questions. This topic is now marked as 'completed'.")
        user_progress[topic] = "completed"
    else:
        print("\nBot: Session ended. This topic remains 'in-progress'.")
        
def take_final_test(topics):
    """
    Conducts a final test on all topics that have been completed.
    """
    print("\n--- Final Test ---")
    print("It's time to check your knowledge! Let's take a final test on the topics you covered.")
    score = 0
    total_questions = len(topics) * 2
    
    for topic in topics:
        for _ in range(2): # 2 questions per topic
            # Get the question and options, but NOT the answer
            prompt_question = f"Generate a unique and different multiple choice question about the topic '{topic}' with four options (A, B, C, D). Ensure the output does NOT contain the correct answer."
            question_data = get_openai_response(prompt_question)
            
            # Get the correct answer separately
            prompt_answer = f"For the question: '{question_data}', what is the correct option? Provide only the option letter (e.g., 'A')."
            correct_answer_letter = get_openai_response(prompt_answer)
            
            print(f"\nQuestion: {question_data}")
            user_test_answer = input("Your Answer (A, B, C, or D): ").upper()
            
            # Check if the user's answer is in the correct answer data
            if user_test_answer in correct_answer_letter:
                print("Correct!")
                score += 1
            else:
                # Get the full correct answer for explanation
                prompt_full_answer = f"For the question: '{question_data}', what is the correct answer? Provide the option letter followed by the correct answer text."
                full_answer = get_openai_response(prompt_full_answer)
                print(f"Incorrect. The correct answer was: {full_answer}")
            time.sleep(1)
                
    print("\n--- Test Results ---")
    print(f"You scored {score} out of {total_questions}.")
    print("Keep up the great work!")

def main():
    """
    The main function that runs the entire program flow.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: The OPENAI_API_KEY environment variable is not set.")
        print("Please ensure your key is correctly configured and restart your terminal/VS Code.")
        return
    
    global client
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"An unexpected error occurred during API initialization: {e}")
        return

    print("------------------------------------------------------------------")
    print("Welcome to PathFinder AI! Your Personalized Study Companion.")
    print("------------------------------------------------------------------")
    subject = input("What do you want to learn today?\nYou: ")
    roadmap_text = generate_roadmap(subject)
    
    # Process the roadmap text into a clean list of topics
    roadmap_topics = [line.split(".")[1].strip().rstrip(':') for line in roadmap_text.split('\n') if line.strip() and line.split(".")[0].isdigit() and line.split(".")[1].strip()]
    
    if not roadmap_topics:
        print("\n--- Error in Roadmap Generation ---")
        print("The API returned an error. Please try again.")
        return
    
    print("\n--- Your Personalized Roadmap ---")
    for i, topic in enumerate(roadmap_topics):
        print(f"{i+1}. {topic}")
    print("-----------------------------------")
    
    print("\nLet's start your learning journey! Choose a topic by entering its number.")
    
    while True:
        completed_topics = [topic for topic, status in user_progress.items() if status == 'completed']
        remaining_topics = [topic for topic in roadmap_topics if topic not in completed_topics]
        
        if not remaining_topics:
            print("\nCongratulations! You have completed all the topics in your roadmap.")
            take_final_test(roadmap_topics)
            break

        print("\n--- Progress ---")
        print(f"Topics Completed: {len(completed_topics)}/{len(roadmap_topics)}")
        
        user_input = input("Enter the number of the topic you want to learn, 'test' for final test, or 'P' to check progress: ")

        if user_input.lower() == 'p':
            print("\n--- Your Current Progress ---")
            for topic in roadmap_topics:
                status = user_progress.get(topic, 'Not Started')
                print(f"- {topic}: {status}")
            continue

        if user_input.lower() == 'test':
            if completed_topics:
                take_final_test(completed_topics)
            else:
                print("You need to complete at least one topic before taking a test.")
        
        else:
            try:
                selected_index = int(user_input) - 1
                if 0 <= selected_index < len(roadmap_topics):
                    selected_topic = roadmap_topics[selected_index]
                    if selected_topic not in completed_topics:
                        conduct_tutoring_session(selected_topic)
                    else:
                        print("This topic is already completed. Please choose a different one.")
                else:
                    print("Invalid number. Please choose a number from the roadmap.")
            except ValueError:
                print("Invalid input. Please enter a number, 'test', or 'P'.")

if __name__ == "__main__":
    main()