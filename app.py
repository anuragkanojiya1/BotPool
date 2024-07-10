import sys
from openai import OpenAI
from mindsdb_sdk.utils.mind import create_mind
from config import api_key

base_url = 'https://llm.mdb.ai/'

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# Mind name to use
mind_name = '_yodb_mind'

try:
    # Check if the mind already exists
    existing_minds = client.beta.minds.list()
    mind_exists = any(mind.name == mind_name for mind in existing_minds.data)

    if not mind_exists:
        mind = create_mind(
            name=mind_name,
            description='Whales',
            base_url=base_url,
            api_key=api_key,
            model='gpt-4',
            data_source_type='postgres',
            data_source_connection_args={
                'user': 'demo_user',
                'password': 'demo_password',
                'host': 'samples.mindsdb.com',
                'port': '5432',
                'database': 'demo',
                'schema': 'demo_data'
            }
        )
        print(f"Created mind: {mind.name}")
    else:
        print(f"Mind {mind_name} already exists. Skipping creation.")
except Exception as e:
    print(f" ")

while True:
    # Proceed with creating a thread and getting responses
    thread = client.beta.threads.create()   

    user_input = input("You: ")

    # Adding prompt template manually
    prompt_template = 'You are Deadpool, give comments on the user input like a therapist Deadpool in his sarcastic and psychotic way: {input}'
    formatted_input = prompt_template.format(input=user_input)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=formatted_input
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=mind_name  # using the name of the database mind
    )

    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        for message in messages.data:
            if message.role == "assistant":
                print(f"Assistant: {message.content[0].text.value}")
            # elif message.role == "user":
            #     print(f"You: {message.content[0].text.value}")
    else:
        print("Assistant did not complete the request. Status:", run.status)

    # Clean up by deleting the thread
    client.beta.threads.delete(thread.id)

    continue_input = input("Do you want another therapy session with Deadpool? (yes/no): ")
    if continue_input.lower() != "yes":
        break

print("Goodbye!")
