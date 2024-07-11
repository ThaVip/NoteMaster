# NoteMaster

![NoteMaster Screenshot](path/to/your/screenshot.png)

## Introduction

Welcome to NoteMaster, a web application designed to streamline note-taking and management. With NoteMaster, you can create, edit, and organize your notes efficiently. This project was developed solo by Musa Sheriff.

- **Deployed Site**: [NoteMaster](https://thavip.github.io/NoteMaster/)
- **Project Blog Article**: [Journey Through Developing NoteMaster](link-to-your-blog-post)
- **Author LinkedIn**: [Musa Sheriff](https://www.linkedin.com/in/musa-sheriff/)

## Installation

To set up NoteMaster locally, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/thavip/NoteMaster.git
    cd NoteMaster
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**

    ```sh
    flask run
    ```

6. **Access the application:**

    Open your browser and go to `http://127.0.0.1:5000`.

## Usage

Once the application is running, you can:

- **Register** a new user account.
- **Log in** with your credentials.
- **Create, edit, and delete notes**.

## Contributing

Contributions are welcome! To contribute to NoteMaster, follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**

    ```sh
    git checkout -b feature/YourFeatureName
    ```

3. **Make your changes and commit them:**

    ```sh
    git commit -m 'Add some feature'
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature/YourFeatureName
    ```

5. **Create a pull request**.

## Related Projects

If you like NoteMaster, you might also be interested in:

- [Evernote](https://evernote.com/)
- [Google Keep](https://keep.google.com/)
- [Microsoft OneNote](https://www.onenote.com/)

## Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


