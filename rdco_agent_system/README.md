# RD&Co Multi-Agent System

This project is an implementation of the multi-agent AI architecture for RD&Co Investment Banking & Financial Advisory.

## Setup and Installation

This project is packaged using `pyproject.toml` and should be installed in a virtual environment.

1.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    ```

2.  **Activate the virtual environment:**
    *   On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```

3.  **Install the project in editable mode:**
    This command installs the project and its dependencies. The `-e` flag allows you to make changes to the source code without reinstalling.
    ```bash
    pip install -e .
    ```

## Running the System

Once the project is installed, you can run the main application loop.

```bash
python main.py
```

## Running Tests

The project uses `pytest` for testing.

1.  **Install testing dependencies (if not already installed):**
    ```bash
    pip install pytest
    ```

2.  **Run the test suite:**
    ```bash
    pytest
    ```
