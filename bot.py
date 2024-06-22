import slack_sdk
import os
from pathlib import Path
from dotenv import load_dotenv 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

chan = '#acon-bot-testing' # channel

client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel=chan, text="bzzz...bzz...testing...")

response = client.chat_postMessage(
    channel=chan,
    thread_ts="1476746830.000003",
    text="Hello from your app! :tada:",
)

times = response["ts"]

client.chat_postMessage(
    channel=chan,
    thread_ts=times,
    text="Hello from your app! :tada:",
)