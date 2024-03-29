# Chat-with-your-Database-Using-Langchain

Welcome to the Interactive Chat System repository! This Python script orchestrates an interactive chat system utilizing AI Language Models (LLMs) from the `langchain` library. It is designed to facilitate seamless interactions with users, leveraging AI capabilities to respond dynamically to input messages. Below is an overview of the repository structure and functionality.

## Repository Structure

- `main.py`: This Python script serves as the main entry point for the interactive chat system. It orchestrates interactions with AI Language Models, manages conversation memory, and executes various functions based on user input.
- `tools/`: This directory contains utility scripts for interacting with SQLite databases and generating reports.
  - `sql.py`: This script provides tools for interacting with a SQLite database, including executing SQL queries and describing table schemas.
  - `report.py`: This script facilitates the generation of HTML reports using structured data and validation tools.

## Functionality

The `main.py` script performs the following tasks:

- **AI Language Model Interaction**: It utilizes the `langchain` library to interact with AI Language Models for responding to user input.
- **SQLite Database Interaction**: The script imports modules for database connectivity and management. It retrieves a list of tables from a SQLite database and constructs a chat prompt template specific to the database environment.
- **Conversation Memory Management**: The script sets up conversation memory to facilitate seamless interactions and maintains context throughout the conversation.
- **Agent Configuration**: An agent is configured to execute various functions using provided tools, such as SQL operations and reporting.
- **Interactive Loop**: Users can input messages, with the system responding accordingly based on the agent's execution and the database schema.

## Running Locally

To run the script locally, follow these steps:

1. Make sure you have Python and pipenv installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the repository directory.
4. Create a `.env` file and set `OPENAI_API_KEY` to your OpenAI API key.
5. Install dependencies using pipenv: `pipenv install`.
6. Run the script using pipenv: `pipenv run python main.py`.

## Sample Databases

For testing purposes, two sample SQLite databases are provided:

- `db.sqlite`: A sample database for an ecommerce website.
- `db_2.sqlite`: A sample database related to music.

Feel free to explore these databases and interact with the chat system!

## Requirements

This project utilizes pipenv for managing dependencies. Make sure you have pipenv installed on your system.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to explore the repository and contribute to its development! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. Thank you for your interest in our interactive chat system!
