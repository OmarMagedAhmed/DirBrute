# DirBrute 📁

A simple Python-based directory bruteforcing tool. It attempts to discover hidden directories and files on a web server by iterating through a user-provided wordlist and checking for valid responses.

### Responsible use
- This tool is intended for **authorized** security testing only (your own systems or systems for which you have explicit permission).
- Misuse of scanning/brute-force tools is illegal and unethical.
- Use responsibly.

### Features ✨
* **Wordlist-Based:** Reads from any provided wordlist file.
* **Simple & Fast:** Sends `GET` requests to discover content.
* **Error Handling:** Ignores connection errors for non-existent targets.
* **Status Codes:** Reports the status code of found resources.

### Prerequisites 📋
To run this tool, you'll need Python 3 and the `requests` library.

You can install the required library using pip:
```bash
pip install requests
```
*(Alternatively, you can use the `requirements.txt` file by running `pip install -r requirements.txt`)*

You will also need a **wordlist** file. A small example, `directories.txt`, is included. For more effective testing, you can use larger, more comprehensive wordlists from projects like [SecLists](https://github.com/danielmiessler/SecLists).

### How to Run 🕹️
1.  **Clone or download** this repository.
2.  **Install prerequisites** as shown above.
3.  **Navigate** to the directory:
    ```bash
    cd /path/to/DirBrute
    ```
4.  **Run the script:**
    ```bash
    python dirbrute.py
    ```
5.  **Follow the prompts:**
    * Enter the target URL (e.g., `example.com` or `http://example.com`)
    * Enter the name of your wordlist file (e.g., `directories.txt`)

### Files
- `dirbrute.py` — main script
- `directories.txt` — sample directory wordlist
- `requirements.txt`
- `LICENSE`
- `README`

### License 📝
This project is open-source and available under the MIT License.