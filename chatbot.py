import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

load_dotenv()
model_name = os.getenv("MODEL", "gpt-3.5-turbo")
llm = init_chat_model(model_name, temperature=0)

# Placeholder med reconciliation tool
def compare_meds(meds_text: str) -> str:
    return f"Medication reconciliation placeholder: compare lists in '{meds_text}' and flag potential discrepancies (mock)"

tools = [
    {"name": "MedCompare", "func": compare_meds, "description": "Compare medication lists and highlight differences"}
]

agent = create_agent(llm, tools=tools, name="AgenticMedRec")

if __name__ == '__main__':
    while True:
        q = input('You: ')
        if q.lower() in ['exit','quit']:
            break
        print('Bot:', agent.run(q))
