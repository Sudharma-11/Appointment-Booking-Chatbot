# Appointment Booking Chatbot

An AI-powered web application for scheduling appointments using natural language interaction (LLM). The LLM helps in making the AI chatbot more conversational and human like responses.

## Features

- Natural language interface for appointment booking
- Automated extraction of user information (name, email, phone, age)
- Real-time display of available appointment slots
- Integration with MySQL database for data persistence
- User-friendly web interface built with Streamlit

## Technologies Used

- Python 3.12 (64-bit)
- Streamlit
- Google Generative AI (Gemini-pro) [LLM model]
- NLP
- MySQL Connector
- Regular Expressions (re module)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/appointment-booking-chatbot.git
   cd appointment-booking-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Create a database named `appointment_db`
   - Run the SQL scripts in `database_setup.sql` to create the necessary tables

4. Configure the database connection:
   - Open `llm.py` and update the database connection details in the `get_db_connection()` function

5. Set up Google Generative AI:
   - Obtain an API key from the Google AI Platform
   - Store your API key in a .env file in the project directory (Recommended)
   - Set the API key in `llm.py`:
     ```python
     API_KEY = 'your_api_key_here'
     ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run front.py
   ```

2. Open a web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)

3. Interact with the chatbot to book an appointment

## Project Structure

- `front.py`: Streamlit web application for the user interface
- `llm.py`: Backend logic for the chatbot, including NLP and database interactions
- `requirements.txt`: List of Python dependencies

## DEMO IMAGES
The sample output images of the appointment booking chatbot are uploaded inside the Demo folder, which is present in the main branch

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
