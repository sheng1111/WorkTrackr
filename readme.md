# 📒WorkTrackr/TODO List

Implement a simple web-based work log and to-do list application.

I want to keep track of what I do every day, so I plan to create a to-do list app to familiarize myself with and learn how to deploy Python Flask applications and use Git.

## Installation

Follow the steps below to install and set up the project:

1. Clone the project code to your local environment:

    ```github
    git clone https://github.com/sheng1111/WorkTrackr.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WorkTrackr
    ```

3. Install the required dependencies:

    ```bash
    pip install sqlite
    pip install -r requirements.txt
    ```

4. Start the project:

    Modify the parameters in "app.py" for deployment on the internet:

    ```python
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port='your-port', debug=True)
    ```

## Usage

### Launching Flask

```bash
python3 app.py
 ```

## Author

😊sheng1111
