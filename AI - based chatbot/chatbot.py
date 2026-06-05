# ============================================================
#  DecodeLabs | Batch 2026 | Project 1: Rule-Based AI Chatbot
#  Author : Divyay Agarwal
#  Built following the IPO Model + Logic Skeleton spec
# ============================================================

import random
import datetime

# ── PHASE 2: KNOWLEDGE BASE (Dictionary → O(1) lookup) ──────
# Using dict instead of if-elif ladder (Anti-Pattern avoided)

knowledge_base = {
    # Greetings
    "hello"       : ["Hey there! 👋 How can I help?",
                     "Hello! Welcome to RuleBot 🤖",
                     "Hi! What can I do for you today?"],
    "hi"          : ["Hey! 👋", "Hi there!", "Hello! 😊"],
    "hey"         : ["Hey! What's up?", "Hey there! 👋"],

    # Identity
    "your name"   : ["I'm RuleBot 🤖 — Project 1 by DecodeLabs!"],
    "who are you" : ["A rule-based chatbot built on pure if-else logic!"],
    "what are you": ["I'm a deterministic AI — no ML, just rules 💡"],

    # Wellbeing
    "how are you" : ["All systems operational! 🤖",
                     "Running perfectly on logic and rules 😄",
                     "Great! Ready to assist you!"],

    # Help
    "help"        : ["I can respond to: greetings, jokes, time, date, "
                     "about, and more! Try typing any of these."],
    "commands"    : ["Try: hello / help / joke / time / date / about / bye"],

    # Jokes
    "joke"        : ["Why do programmers prefer dark mode? "
                     "Because light attracts bugs! 🐛",
                     "Why did the array start at 0? "
                     "It wanted to be different! 😄",
                     "How many devs to change a bulb? "
                     "None — it's a hardware problem! 💡"],

    # About the project
    "about"       : ["This is Project 1 of DecodeLabs AI Internship — "
                     "a Rule-Based Chatbot using Python control flow!"],
    "decodelabs"  : ["DecodeLabs is an AI training org from Greater Lucknow, India 📍"
                     " | www.decodelabs.tech"],

    # Farewell — EXIT STRATEGY (clean break command)
    "bye"         : ["Goodbye! Keep building! 👋",
                     "See you! Keep coding 🚀",
                     "Bye! Project 1 complete 🏆"],
    "exit"        : ["Exiting RuleBot... Goodbye! 👋"],
    "quit"        : ["Shutting down. Bye! 👋"],
}

# ── FALLBACK RESPONSES ───────────────────────────────────────
fallback = [
    "I don't understand that yet. Try typing 'help'! 🤔",
    "That's outside my rules. Type 'commands' to see what I know.",
    "I'm a rule-based bot — I only know predefined responses!",
]

# ── SPECIAL LIVE RESPONSES ───────────────────────────────────
def get_live_response(clean_input):
    if "time" in clean_input:
        return f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')} ⏰"
    if "date" in clean_input or "today" in clean_input:
        return f"Today: {datetime.datetime.now().strftime('%A, %d %B %Y')} 📅"
    return None

# ── PHASE 1: INPUT SANITIZATION ─────────────────────────────
def sanitize(raw_input):
    return raw_input.lower().strip()   # Normalization as per spec

# ── PHASE 2: INTENT MATCHING (Dictionary O(1) Lookup) ────────
def get_response(clean_input):

    # Check live responses first (time/date)
    live = get_live_response(clean_input)
    if live:
        return live

    # Dictionary lookup — O(1) instead of O(n) if-elif ladder
    for key in knowledge_base:
        if key in clean_input:
            return random.choice(knowledge_base[key])

    # FALLBACK — default response for unknowns
    return random.choice(fallback)

# ── PHASE 3: OUTPUT + MAIN LOOP (The Heartbeat) ──────────────
def main():
    print("=" * 55)
    print("   DecodeLabs | Project 1: Rule-Based AI Chatbot 🤖")
    print("   Batch 2026  |  Type 'bye' or 'exit' to quit")
    print("=" * 55)
    print("RuleBot: Hello! I am RuleBot. Type 'help' to start.\n")

    # ── INFINITE LOOP — organism stays alive until kill command
    while True:

        # PHASE 1 — Raw Input
        raw_input = input("You: ")

        # Handle empty input
        if not raw_input.strip():
            print("RuleBot: Please type something!\n")
            continue

        # PHASE 1 — Sanitization (lower + strip)
        clean_input = sanitize(raw_input)

        # EXIT STRATEGY — clean break command
        if clean_input in ["bye", "exit", "quit"]:
            print(f"RuleBot: {random.choice(knowledge_base[clean_input])}\n")
            break   # ← KILL COMMAND

        # PHASE 2 — Intent Matching & Response
        response = get_response(clean_input)

        # PHASE 3 — Output
        print(f"RuleBot: {response}\n")


if __name__ == "__main__":
    main()
