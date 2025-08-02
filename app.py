from flask import Flask, request, render_template
import random
import os

app = Flask(__name__)

def is_malayalam(text):
    return any('ഀ' <= char <= 'ൿ' for char in text)
# Sarcastic replies
malayalam_responses = [
    "അതെ, എനിക്ക് ഇതൊന്നും അറിയില്ല. എന്റെ പേര് തന്നെ മറന്നുപോയി.",
    "ഞാൻ ഒരു ബോട്ട് ആണ്. നിങ്ങൾക്ക് അനുയോജ്യമായ ഉത്തരം കിട്ടുമോ എന്നറിയില്ല.",
    "പഠിച്ച് വരൂ, പിന്നെ വരൂ!",
    "അറിയില്ലല്ലോ... കുഴപ്പമുണ്ടോ?",
    "ഞാനോ അതറിയേണ്ടത്? എനിക്ക് വേറെ വേലകളുണ്ട്.",
]


english_responses = [
    "Seriously? You expect *me* to know that? 🙃",
    "I’m just a bot, not your tutor 🤖",
    "Nice question. No clue 😐",
    "Ask Google. I’m busy being useless 😌",
    "I don’t know, and I’m proud of it 💅",
    "Try switching it off and on again. Classic. 🔌",
]

# Bonus modes
useless_quotes = [
    "Even a stopped clock is right twice a day. Not me though. 😌",
    "Wisdom begins when you realize I know nothing.",
    "Why know the answer when you can pretend you’re mysterious?",
    "Knowledge is power. I am powerless.",
]

wrong_answers = [
    "The answer is 42. Always.",
    "Try unplugging it and plugging it back in.",
    "Banana.",
    "Ask your mom. She probably knows.",
    "According to NASA... nope, still wrong.",
]

emojis = ["😐", "🤡", "🫠", "🤖", "🙃", "🧠", "🥴"]

def generate_reply(is_ml):
    # 20% chance for overload message
    if random.random() < 0.2:
        return "System overload. Please try a dumber question. 🧠🔥"

    # 20% chance to give useless wisdom
    if random.random() < 0.2:
        return random.choice(useless_quotes) + " " + random.choice(emojis)

    # 10% chance for hilariously wrong answer
    if random.random() < 0.1:
        return random.choice(wrong_answers) + " " + random.choice(emojis)

    # Normal sarcastic replies
    base = malayalam_responses if not is_ml else english_responses
    return random.choice(base) + " " + random.choice(emojis)

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = ""
    if request.method == 'POST':
        user_question = request.form.get('question', '')
        is_ml = is_malayalam(user_question)
        answer = generate_reply(is_ml)
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

