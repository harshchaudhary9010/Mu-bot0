import time
from datetime import datetime
import random

# ==============================================================
# PROJECT: UNIVERSITY ASSISTANT CHATBOT (V3.0 - FINAL)
# DEVELOPED BY: HARSH CHAUDHARY | SECTION: A | BCA 6TH SEM
# ENROLLMENT NO: 20230170 | COLLEGE: MANGALAYATAN UNIVERSITY
# ==============================================================

# Data Dictionary
responses = {
    "hi": "Hello Harsh! How can I help you today?",
    "hello": "Hi there! MU BCA Assistant at your service.",
    "who created you?": "I was developed by Harsh Chaudhary, BCA 6th Sem, Section A.",
    "your name?": "I am the MU Assistant Bot (Version 3.0).",
    "enrollment number?": "Your enrollment number is 20230170.",
    "college name?": "Mangalayatan University.",
    "exam dates?": "BCA 6th Sem exams are expected in June. Please check the MU portal.",
    "bye": "Goodbye Harsh! Take care of your family and all the best."
}

quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal.",
    "Coding is the language of the future!",
    "Stay focused and never give up."
]

def run_chatbot():
    print("==================================================")
    print("   MANGALAYATAN UNIVERSITY - BCA PROJECT (V3)     ")
    print("   Developed by: Harsh Chaudhary (Section A)      ")
    print("==================================================")
    print(" COMMANDS: 'time', 'calculate', 'quote', 'search', 'news', 'about' ")
    print("(Type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("Bot:", responses["bye"])
            break

        # COMMAND 1: About Creator (Personal Touch)
        elif "about" in user_input:
            print("Bot: This project is created by Harsh Chaudhary. Enrollment: 20230170. College: Mangalayatan University.")

        # COMMAND 2: News/Updates (Fake University Updates)
        elif "news" in user_input or "update" in user_input:
            updates = [
                "New Seminar on AI & ML scheduled for next Friday.",
                "University library timings extended till 8 PM.",
                "BCA Final Project submission deadline updated on portal."
            ]
            print(f"Bot: [LATEST UPDATE] {random.choice(updates)}")

        # COMMAND 3: Search Simulation (BCA Topics)
        elif "search" in user_input:
            query = input("Bot: What topic do you want to search? ")
            print(f"Bot: Searching for '{query}' in University Database...")
            time.sleep(1.5)
            print(f"Bot: Result found: {query} is a key topic in the BCA 6th Semester curriculum.")

        # COMMAND 4: Calculator
        elif "calculate" in user_input or "solve" in user_input:
            print("Bot: Enter math problem (e.g., 50 + 20):")
            calc = input("Math: ")
            try:
                print(f"Bot: The answer is {eval(calc)}")
            except:
                print("Bot: Sorry, invalid calculation.")

        # COMMAND 5: Date & Time
        elif "time" in user_input or "date" in user_input:
            now = datetime.now()
            print(f"Bot: Today is {now.strftime('%d-%m-%Y')} and time is {now.strftime('%H:%M:%S')}")

        # COMMAND 6: Quote
        elif "quote" in user_input:
            print(f"Bot: {random.choice(quotes)}")

        # Default Matching
        else:
            found = False
            for key in responses:
                if key in user_input:
                    print(f"Bot: {responses[key]}")
                    found = True
                    break
            
            if not found:
                print("Bot: Try 'search', 'news', 'calculate', or 'about'.")

if __name__ == "__main__":
    run_chatbot()
