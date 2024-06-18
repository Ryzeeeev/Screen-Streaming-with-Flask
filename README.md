# Screen Streaming with Flask

This project streams the screen of your computer using Flask and OpenCV. It captures the screen and sends the frames as a video feed through a web server.

## Features

- Captures the screen in real-time.
- Streams the video feed to a web browser.
- Uses Flask for the web server and OpenCV for image processing.

## Requirements

- Python 3.x
- Flask
- OpenCV
- Pillow (PIL)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/screen-streaming-flask.git
    cd screen-streaming-flask
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script**:
    ```sh
    python app.py
    ```

2. **Open your web browser** and navigate to:
    ```
    http://localhost:5000/video_feed
    ```

    This will display the live stream of your screen.

## Code Explanation

- `generate_frames()`: Captures the screen and converts it to a format suitable for streaming.
- `/video_feed` route: Provides the video stream to the browser.

## Troubleshooting

- Make sure no other application is using port 5000.
- If you encounter any issues with dependencies, ensure they are properly installed using `pip install -r requirements.txt`.
- For best performance, run the script on a machine with sufficient resources.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
