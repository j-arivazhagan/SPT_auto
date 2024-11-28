# SPT_auto
SSH Automation for Penetration Testing (Segmentation PT)


---

# **SSH Automation with Nmap**
This web application allows you to automate SSH login to a jump server, fetch `ifconfig` details, and run custom `nmap` commands. The results are saved as `.txt` files, and live notifications are displayed on the web page.

---

## **Project Requirements**

### **1. Required Files**
- **`app.py`**: Main Python file containing the Flask application logic.
- **`templates/index.html`**: Frontend file for the user interface.
- **`static/`**: Directory containing CSS and JavaScript files for styling and functionality.
- **`requirements.txt`**: List of Python packages required to run the application.
- **`output/`**: Directory where `ifconfig` and `nmap` outputs are saved.

---

### **2. Required Packages**

Make sure you have Python 3 installed. Install the following packages using `pip`:

- **Flask**: For creating the web application.
- **paramiko**: For SSH connections.
- **Werkzeug**: For secure file uploads.

Install all dependencies with:
```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```text
flask
paramiko
werkzeug
```

---

### **3. Additional Requirements**
- **SSH Key File**: For servers that require `.pem` or `.ppk` files for login.
- **Nmap**: Ensure `nmap` is installed on the jump server for running scans.

---

## **Usage Instructions**

### **1. Set Up the Project**

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### **2. Run the Application**

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

### **3. Using the Application**

1. **Login to Jump Server**:
   - Enter the **IP/Host**, **Username**, **Port**, and **Password**, or upload a `.pem`/`.ppk` file.
   - Click "Login".

2. **Fetch `ifconfig` Details**:
   - Click the "Fetch `ifconfig`" button.
   - The output will be saved in `output/ifconfig_<timestamp>.txt`.

3. **Run Custom Nmap Command**:
   - Enter your `nmap` command in the input field (e.g., `nmap -sV -p 22,80,443`).
   - Click "Run Nmap".
   - The output will be saved in `output/nmap_<timestamp>.txt`.

4. **View Live Notifications**:
   - Check the top-right corner of the page for status updates like "Logged in", "Fetching `ifconfig`", "Running nmap", etc.

---

## **Folder Structure**

```
project/
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── output/                 # Output files saved here
│   ├── ifconfig_<timestamp>.txt
│   └── nmap_<timestamp>.txt
├── templates/
│   └── index.html          # Frontend template
├── static/
│   ├── style.css           # Styling
│   └── script.js           # JavaScript for live notifications
└── .gitignore              # Ignore unnecessary files in Git
```

---

## **Common Issues and Solutions**

### **1. Error: `ModuleNotFoundError: No module named 'flask'`**
- Ensure you’ve activated the virtual environment and installed dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### **2. Error: `Login failed: Not a valid RSA private key file`**
- Ensure the uploaded `.pem` or `.ppk` file is valid.
- Double-check permissions on the server.

### **3. Nmap Command Not Found**
- Install `nmap` on the jump server:
  ```bash
  sudo apt-get install nmap       # For Ubuntu/Debian
  yum install nmap                # For CentOS/RHEL
  ```

### **4. Web Page Does Not Update**
- Clear your browser cache or refresh the page.
- Check if the Flask app is running and accessible at `http://127.0.0.1:5000`.

---

Let me know if you need further clarification or additional instructions!
