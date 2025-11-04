import os
import time
from how.how_agent import agent
from how.utils.config_utils import config
from how.utils.response_utils import parse_response  # assuming your parse function lives here

TEST_QUESTIONS = [
    "how do I zip all .txt files in the current directory?",
    "how can I find all .py files containing the word 'config'?",
    "how do I check which port is using process 8080?",
    "how do I make a file executable?",
    "how can I show hidden files in this directory?",
    "how do I create and activate a Python virtual environment?",
    "how do I see the last 20 lines of a log file?",
    "how do I kill a process by name?",
    "how can I see the current Git branch?",
    "how do I count the number of lines in a file?",
]

LOG_DIR = os.path.expanduser("~/.config/how2")
LOG_FILE = os.path.join(LOG_DIR, "test_results.txt")


def run_tests():
    os.makedirs(LOG_DIR, exist_ok=True)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"HOW Assistant Test Results — {time.ctime()}\n")
        f.write("=" * 60 + "\n\n")

        for i, question in enumerate(TEST_QUESTIONS, start=1):
            print(f"🧩 Test {i}: {question}")
            try:
                response = agent.ask(question)
                command = parse_response(response)
                if command:
                    print(f"✅ Command: {command}\n")
                    f.write(f"{i}. {question}\nCOMMAND: {command}\n\n")
                    config.log_history(question=question, command=command)
                else:
                    print(f"⚠️ No command parsed.\n")
                    f.write(f"{i}. {question}\nNO COMMAND PARSED\n\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")
                f.write(f"{i}. {question}\nERROR: {e}\n\n")

    print(f"\n📄 Results saved to: {LOG_FILE}")


if __name__ == "__main__":
    run_tests()
