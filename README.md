## Installation

1. Make sure you have Python installed locally.

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv           # Create a virtual environment
    source venv/bin/activate      # Activate the virtual environment (for Linux/Mac)
    .\venv\Scripts\activate       # Activate the virtual environment (for Windows)
    ```

3. Navigate to the directory:
    ```bash
    cd gvmg
    ```

4. Run the script:
    ```bash
    scrapy crawl gvmgspider -o articles.json
    ```

Ensure you have Scrapy installed locally (after the venv activation) to run the script properly.
