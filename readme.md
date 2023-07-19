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
        app.run(host='0.0.0.0', port='your-port', debug=False)
    ```

## Usage

### Launching Flask

```bash
python3 app.py
 ```

### APP-Preview

![index](https://github.com/sheng1111/WorkTrackr/assets/37472419/5e22fefd-d3e7-4e90-a2d7-3e6fec44585b)

![record](https://github.com/sheng1111/WorkTrackr/assets/37472419/bac1a166-389b-4ba2-bd53-a68b12406971)

![todo list](https://github.com/sheng1111/WorkTrackr/assets/37472419/7d5d100d-e82d-461d-bffe-8f3b1bd1d2d8)

![search](https://github.com/sheng1111/WorkTrackr/assets/37472419/79d8fd57-9bcf-48a4-9e66-c712d00d2295)

## Author

😊sheng1111
