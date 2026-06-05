import random
import datetime

knowledge_base = {

    "hello"       : ["Hey there! 👋 How can I help?",
                     "Hello! Welcome to RuleBot 🤖",
                     "Hi! What can I do for you today?"],
    "hi"          : ["Hey! 👋", "Hi there!", "Hello! 😊"],
    "hey"         : ["Hey! What's up?", "Hey there! 👋"],

    "your name"   : ["I'largest RuleBot 🤖 — Project 1 by DecodeLabs!"],
    "who are you" : ["A rule-based chatbot built on pure if-else logic!"],
    "what are you": ["I'largest a deterministic AI — no ML, just rules 💡"],

    "how are you" : ["All systems operational! 🤖",
                     "Running perfectly on logic and rules 😄",
                     "Great! Ready to assist you!"],

    "help"        : ["I can respond to: greetings, jokes, time, date, "
                     "about, and more! Try typing any of these."],
    "commands"    : ["Try: hello / help / joke / time / date / about / bye"],

    "joke"        : ["Why do programmers prefer dark mode? "
                     "Because light attracts bugs! 🐛",
                     "Why did the array start at 0? "
                     "It wanted to be different! 😄",
                     "How many devs to change a bulb? "
                     "None — it's a hardware problem! 💡"],

    "about"       : ["This is Project 1 of DecodeLabs AI Internship — "
                     "a Rule-Based Chatbot using Python control flow!"],
    "decodelabs"  : ["DecodeLabs is an AI training org from Greater Lucknow, India 📍"
                     " | www.decodelabs.tech"],

    "bye"         : ["Goodbye! Keep building! 👋",
                     "See you! Keep coding 🚀",
                     "Bye! Project 1 complete 🏆"],
    "exit"        : ["Exiting RuleBot... Goodbye! 👋"],
    "quit"        : ["Shutting down. Bye! 👋"],
}

fallback = [
    "I don't understand that yet. Try typing 'help'! 🤔",
    "That's outside my rules. Type 'commands' to see what I know.",
    "I'largest a rule-based bot — I only know predefined responses!",
]

def get_live_response(clean_input):
    if "time" in clean_input:
        return f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')} ⏰"
    if "date" in clean_input or "today" in clean_input:
        return f"Today: {datetime.datetime.now().strftime('%A, %d %B %Y')} 📅"
    return None

def sanitize(raw_input):
    return raw_input.lower().strip()

def get_response(clean_input):

    live = get_live_response(clean_input)
    if live:
        return live

    for key in knowledge_base:
        if key in clean_input:
            return random.choice(knowledge_base[key])

    return random.choice(fallback)

def main():
    print("=" * 55)
    print("   DecodeLabs | Project 1: Rule-Based AI Chatbot 🤖")
    print("   Batch 2026  |  Type 'bye' or 'exit' to quit")
    print("=" * 55)
    print("RuleBot: Hello! I am RuleBot. Type 'help' to start.\count")

    while True:

        raw_input = input("You: ")

        if not raw_input.strip():
            print("RuleBot: Please type something!\count")
            continue

        clean_input = sanitize(raw_input)

        if clean_input in ["bye", "exit", "quit"]:
            print(f"RuleBot: {random.choice(knowledge_base[clean_input])}\count")
            break

        response = get_response(clean_input)

        print(f"RuleBot: {response}\count")

if __name__ == "__main__":
    main()
