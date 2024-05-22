from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import os
import docx

# Initialize bot with token
TOKEN = "xxxxxxxxxxxx"  # Replace with your actual bot token

# Specify the path to the folder containing the questions
folder_path = r"C:\Users\Aditya\Desktop\DevOps\Questions"

def read_questions_from_word_files(folder_path):
    """
    Reads questions from .docx files in the specified folder.

    Args:
        folder_path (str): The path to the folder containing the .docx files.

    Returns:
        list: A list of questions extracted from the .docx files.
    """
    questions = []
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".docx"):
                doc_path = os.path.join(folder_path, filename)
                doc = docx.Document(doc_path)
                for paragraph in doc.paragraphs:
                    question_text = paragraph.text.strip()
                    if question_text:  # Only consider non-empty lines as questions
                        questions.append(question_text)
    except Exception as e:
        print(f"An error occurred while reading the files: {e}")
    return questions

# Populate the questions list
questions = read_questions_from_word_files(folder_path)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Sends a random question to the Telegram chat.

    Args:
        update (Update): The Telegram update object.
        context (ContextTypes.DEFAULT_TYPE): The Telegram callback context.
    """
    if questions:
        random_question = random.choice(questions)
        await update.message.reply_text(random_question)
    else:
        await update.message.reply_text("No questions available.")

def main() -> None:
    """
    The main function to start the Telegram bot.
    """
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()

if __name__ == '__main__':
    main()
