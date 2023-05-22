# IMDb Top 100 Movie Scraper

This Python script utilizes the BeautifulSoup4 library to scrape the IMDb Top 100 chart and randomly selects a movie from the list. The project is containerized using Docker, allowing for easy deployment and execution in any environment.

## Requirements

- Python 3.x
- Docker (optional, for containerized execution)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Veluthil/Top-100-IMDb-Movies-Docker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Top-100-IMDb-Movies-Docker
   ```

3. Install the required Python dependencies:

   ```bash
   pip install -r requests beautifulsoup4
   ```

## Usage

### Running the Script

1. Execute the Python script:

   ```bash
   python main.py
   ```

   This will scrape the IMDb Top 100 chart and randomly select a movie from the list. The movie title and details will be displayed in the console.

### Running with Docker (optional)

1. Build the Docker image (you can call it however you like):

   ```bash
   docker build -t imdb-top-100-scraper .
   ```

2. Run the Docker container:

   ```bash
   docker run -t -i imdb-top-100-scraper
   ```

   This will execute the Python script inside the Docker container, providing the same functionality as running the script directly.

## Customization

If you wish to modify the script or add additional features, you can easily do so by editing the `main.py` file. The script uses BeautifulSoup4 and requests to scrape the IMDb website and the `random` module to select a movie randomly.

## Acknowledgements

- This project utilizes the BeautifulSoup4 library: [https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/)
- Also requests library: [https://pypi.org/project/requests/](https://pypi.org/project/requests/)
- IMDb website: [https://www.imdb.com/](https://www.imdb.com/)

## Disclaimer

This project is for educational and personal use only. The scraping of websites may be subject to legal restrictions, and it is the responsibility of the user to ensure compliance with applicable laws and regulations.