class OpenAIAssistant:
    client = None
    assistant = None
    thread = None

    def __init__(self, client):
        self.client = client
        self.assistant = client.beta.assistants.create(
            name="API Caller",
            instructions="You are responsible for handling apis for a particular website which will be given by the user. User will give instructions to do particular tasks like 'Add To Cart' 'Tell me the items present in the inventory' 'How many categories are there' ",
            model="gpt-3.5-turbo-0125",
        )
        self.thread = client.beta.threads.create()

    def add_message(self, role, content):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id, role=role, content=content
        )

    def create_run(self):
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id, assistant_id=self.assistant.id
        )
        if run.status == 'completed':
            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id
            )
            print(messages)
        else:
            print(run.status)
