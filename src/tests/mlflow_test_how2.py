import json
import mlflow
import time
from how.how_agent import agent
from how.utils.config_utils import config

EXPERIMENT_NAME = "how_agent_tests"
mlflow.set_experiment(EXPERIMENT_NAME)
mlflow.set_tracking_uri("file:///Users/dan/Code/Vibe_Coding/how/mlruns")

# ------------------------------------------
# Test questions
# ------------------------------------------
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

# ------------------------------------------
# Run tests
# ------------------------------------------
for question in TEST_QUESTIONS:
    run_name = f"{time.strftime('%Y%m%d-%H%M%S')} | {question[:30]}"
    with mlflow.start_run(run_name=run_name) as run:
        print(f"\n🧩 Running question: {question}")

        # Log input parameters
        mlflow.log_param("question", question)
        mlflow.log_param("model_name", config.get("model_name"))
        mlflow.log_param("temperature", config.get("temperature"))

        try:
            # Ask the agent
            response = agent.generate_response(question)
            print(f"Response: {response}")

            if not response:
                mlflow.log_metric("success", 0)
                mlflow.log_text("No response generated", "responses/raw_response.txt")
                continue

            # Attempt to parse JSON
            try:
                data = json.loads(response)
            except json.JSONDecodeError:
                mlflow.log_metric("success", 0)
                mlflow.log_text(response, "responses/raw_response.txt")
                print("⚠️ Failed to parse JSON response")
                continue

            resp_type = data.get("type")
            content = data.get("content")
            comment = data.get("comment", None)

            # Handle response types
            if resp_type == "question":
                mlflow.log_metric("success", 1)
                mlflow.log_text(content, "responses/parsed_answer.txt")
                print(f"💡 Answer: {content}")

            elif resp_type == "command":
                mlflow.log_metric("success", 1)
                mlflow.log_text(content, "responses/parsed_command.txt")
                if comment:
                    mlflow.log_text(comment, "responses/comment.txt")
                # Add to history
                config.log_history(question=question, command=content)
                print(f"💻 Command: {content}")
                if comment:
                    print(f"⚠️ Comment: {comment}")

            else:
                mlflow.log_metric("success", 0)
                mlflow.log_text(json.dumps(data), "responses/unknown_response.txt")
                print("⚠️ Unknown response type")

        except Exception as e:
            mlflow.log_metric("success", 0)
            mlflow.log_text(str(e), "responses/error.txt")
            print(f"❌ Exception for question '{question}': {e}")

print("\n📄 MLflow test run complete.")
print("Use `mlflow ui` to view results at http://127.0.0.1:5000")
