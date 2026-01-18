# Shadow Portfolio

A modern, Django-based portfolio application designed to showcase projects, updates, and provide a means of contact.

## 🚀 Features

*   **Portfolio Showcase**: distinct section to display projects (`apps/core`).
*   **Updates/Blog**: A system to post regular updates or blog entries (`apps/updates`).
*   **Contact Form**: A fully functional contact form to get in touch (`apps/contact`).
*   **Responsive Design**: Built with custom HTML/CSS for a unique look.

## 🛠 Technology Stack

*   **Backend**: Python, Django 4.2
*   **Server**: Gunicorn
*   **Static Files**: WhiteNoise
*   **Database**: SQLite (Development), DJ-Database-URL supported
*   **Frontend**: HTML5, CSS3, JavaScript

## 📦 Installation

 Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone <https://github.com/abhi-abhi86/shadow.git>
    cd shadow
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r my_portfolio/requirements.txt
    ```

4.  **Set up environment variables:**
    You can export these in your shell or create a `.env` file if you configure `python-dotenv`.
    *   `SECRET_KEY`: A secret string for Django security.
    *   `DEBUG`: Set to `True` for development.

5.  **Apply migrations:**
    ```bash
    python my_portfolio/manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python my_portfolio/manage.py runserver
    ```

    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the application.

## 📂 Project Structure

*   `my_portfolio/`: Main project directory.
    *   `apps/`: Contains the Django applications.
        *   `core/`: Main functionality (Home, Projects).
        *   `contact/`: Contact form and logic.
        *   `updates/`: Blog/Updates functionality.
    *   `config/`: Project settings and configuration.
    *   `static/`: CSS, JS, and images.
    *   `templates/`: HTML templates.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
