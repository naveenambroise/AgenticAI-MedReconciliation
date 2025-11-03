import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import chatbot

QUERIES = [
    "Compare medication lists: List A = [aspirin 81mg], List B = [aspirin 81mg, vitamin D]",
    "Flag potential drug interactions for [warfarin, ibuprofen]",
]

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_PATH = os.path.join(LOG_DIR, 'medrec_chat_log.txt')

with open(LOG_PATH, 'a', encoding='utf-8') as f:
    for q in QUERIES:
        ts = datetime.utcnow().isoformat() + 'Z'
        try:
            r = chatbot.agent.run(q)
            print('Q:', q)
            print('R:', r)
            f.write(f'[{ts}] Q: {q}\n')
            f.write(f'[{ts}] R: {r}\n\n')
        except Exception as e:
            print('Error:', e)
            f.write(f'[{ts}] Q: {q}\n')
            f.write(f'[{ts}] ERROR: {e}\n\n')
