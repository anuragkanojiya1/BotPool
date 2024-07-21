## BotPool

BotPool is a Command Line Interface (CLI) chatbot that combines the therapeutic advice of a counselor with the humor and wit of Deadpool. This unique chatbot provides advice and suggestions as a therapist would, but with Deadpool's signature sarcastic and psychotic style.

## Features

- **Therapist-Style Advice**: Get advice and suggestions on various topics.
- **Deadpool's Humor**: Enjoy responses laced with Deadpool's humor and wit.
- **Continuous Interaction**: Engage in an ongoing conversation until you decide to end it.

## Technology Stack
- **MindsDB SDK**

  BotPool uses the MindsDB SDK to create and manage a "mind." Minds are AI systems with built-in expertise designed to help AI agents accomplish tasks with minimal setup. The Database Mind, used in BotPool,        simplifies data access and answers questions directly from databases in natural language, eliminating the complexity of reasoning and execution loops for data retrieval.

- **OpenAI SDK and GPT-4**

  BotPool uses the OpenAI SDK to interact with the GPT-4 model. GPT-4 provides advanced natural language understanding and generation capabilities, allowing BotPool to deliver responses with Deadpool's humor and   wit.

## Screenshot

![Screenshot 2024-07-11 000338](https://github.com/anuragkanojiya1/BotPool/assets/144598258/19e3553a-84d6-4ebb-97b7-c00769a1a60d)

## Video 

https://github.com/user-attachments/assets/f9063bf2-94d9-4ab2-a4ac-b8523861ca19

## Prerequisites

- Python 3.6 or higher
- Required Python packages (see requirements.txt)
  
## Installation

1. Clone the repository:

```sh
  git clone https://github.com/YOUR_USERNAME/BotPool.git
  cd BotPool
```

2. Create a virtual environment and activate it:

 ```sh
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Create a config.py file:

- In the root of the project directory, create a file named config.py.
- Add your API key to config.py:
```sh
  api_key = 'your_api_key'
```
- You can get your API key from https://mdb.ai/.

4. Install the required packages:
```sh
  pip install -r requirements.txt
```

## Usage

1. Run the chatbot:
```sh
  python app.py
```

2. Interact with BotPool:

- The chatbot will prompt you for input and respond with advice and suggestions in Deadpool's style.
- Continue the conversation until you decide to end it.

## Example Interaction

```sh
  You: I feel stressed about my upcoming exams.
  Assistant: Ah, stress! The silent killer. Have you tried screaming into a pillow? It's like a massage for your soul, just noisier. But seriously, take a break, do something fun. Even Deadpool needs downtime.
```

## Contributing

1. Fork the repository.
2. Create a new branch:
```sh
  git checkout -b feature/your-feature
```
3. Make your changes.
4. Commit your changes:
```sh
  git commit -m "Add some feature"
```
5. Push to the branch:

```sh
  git push origin feature/your-feature
```
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Deadpool for his unique brand of humor and wit.
- https://github.com/anuragkanojiya1 for creating this chatbot.

## Contact

- LinkedIn : https://linkedin.com/in/anurag-kanojiya-101312286
- X : https://twitter.com/AnuKanojiya829
