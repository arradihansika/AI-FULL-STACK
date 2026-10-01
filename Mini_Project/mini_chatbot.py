from ollama import chat

system_msg = "You are my friendly tutor. Answer in warm tones. Answer in one sentence."
history = [{"role" : "system", "content" : system_msg}]
question_counter = 0

print("Sharanya 🤖: Nice to meet you, Hansika!!")
while True:
    question = input("You:")
    if question == "":
        print("Sharanya 🤖: Please try something.")
        continue

    if question.lower().strip() == "/clear":
        history = [{"role" : "system", "content" : system_msg}]
        print("Your history is cleared.Start a fresh conversation.")
        print()
        continue

    if question.lower().strip() == "/help":
        print("------ Available Commands ------")
        print("/history - displays conversation history")
        print("/clear - clear chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("--------------------------------")
        print()
        continue 
#

    if question.lower().strip() == "/history":
        print("----- Your Conversation so far -----")
        if len(history) < 2:
            print("Nothing so far!")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Sharanya 🤖"
            print(f"{speaker}: {msg['content']}")
            print("-------------------------------")
            print()
            continue

    if question.lower().strip() == "exit":
        print("Sharanya 🤖: GoodBye user.Please come back soon!😘")
        print(f"You asked {question_counter} questions today.Good job!")
        break
    history.append({"role" : "system", "content" : question})
    question_counter += 1
    try:
        response = chat(
                model="llama3.2",
                messages = history
            )
        reply = response.message.content
        history.append({"role" : "system", "content" : reply})
        print(f"Sharanya 🤖:{reply}")
        print()
    except Exception as e:
        print("Unknown issue.Is Ollama running?")
