<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Secure DocVault - AI Encrypted Document Management System</title>
</head>
<body>

<h1>🔐 Secure DocVault</h1>

<blockquote>
  <em>A secure, AI-enhanced document management system featuring AES-256 encrypted storage, role-based access control (RBAC), two-factor authentication (2FA), and a web interface for uploading, managing, and searching encrypted files.</em>
</blockquote>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>🔒 AES-256 Encrypted Filesystem</li>
  <li>🔑 Role-Based Access Control (Admin, Editor, Viewer)</li>
  <li>🔐 Two-Factor Authentication (TOTP 2FA)</li>
  <li>📚 Document Upload and Secure Storage</li>
  <li>🔎 AI-Enhanced Semantic Search using LLM Embeddings (FAISS + Sentence Transformers)</li>
  <li>🧩 Flask Web Interface (Login, Upload, View, Search)</li>
  <li>🛡️ Secure Session Management</li>
  <li>⚡ Minimalistic, Professional Web Design</li>
</ul>

<hr>

<h2>📂 Project Folder Structure</h2>

<pre><code>
secure_docvault/
├── README.html           # Project documentation (this file)
├── setup.sh              # Automatic environment and database setup script
├── requirements.txt      # Python dependency list
│
├── config/
│   └── settings.py       # Configuration (encryption keys, 2FA secret, RBAC)
│
├── core/
│   ├── encryptor.py      # AES-256 file encryption and decryption
│   ├── auth.py           # User login and 2FA verification
│   ├── access_control.py # Role-based access checking
│   ├── document_store.py # Handling document storage (save, load)
│   ├── llm_indexer.py    # LLM-based document embedding and search
│   ├── build_vectorstore.py # Script to generate initial semantic search index
│   └── utils.py          # Helper functions (hashing, token generation, filename sanitizing)
│
├── data/
│   ├── vault/            # Encrypted folder and document storage
│   └── users.json        # User database (hashed passwords, roles)
│
├── models/
│   └── vectorstore.pkl   # Saved FAISS vector index for LLM search
│
├── web/
│   ├── __init__.py       # Flask app factory (if modularizing)
│   ├── app.py            # Flask application server
│   ├── forms.py          # Login form (username, password, 2FA)
│   ├── xforms.py         # Upload, Folder Creation, Search forms
│   ├── templates/
│   │   ├── login.html    # Login page
│   │   ├── index.html    # Folder browser page
│   │   ├── folder.html   # Document listing page
│   │   ├── upload.html   # Upload document page
│   │   ├── search.html   # Search query page
│   ├── static/
│   │   └── style.css     # Frontend CSS styling
</code></pre>

<hr>

<h2>📜 File-by-File Overview</h2>

<ul>
  <li><strong>setup.sh:</strong> Automatically installs dependencies, sets up environment, generates encryption keys and creates default users.</li>
  <li><strong>requirements.txt:</strong> List of Python packages (Flask, cryptography, pyotp, langchain, sentence-transformers, faiss).</li>
  <li><strong>config/settings.py:</strong> Application configuration including Flask secret key, encryption key, 2FA seed, and role permissions.</li>
  <li><strong>core/encryptor.py:</strong> Handles AES-256 encryption and decryption of document contents.</li>
  <li><strong>core/auth.py:</strong> Verifies user credentials and TOTP 2FA tokens.</li>
  <li><strong>core/access_control.py:</strong> Enforces role-based permissions for file and folder actions.</li>
  <li><strong>core/document_store.py:</strong> Save and load documents inside the encrypted filesystem.</li>
  <li><strong>core/llm_indexer.py:</strong> Encodes documents into embeddings and saves a searchable FAISS index.</li>
  <li><strong>core/build_vectorstore.py:</strong> Script to initially build <code>vectorstore.pkl</code> after uploading documents.</li>
  <li><strong>core/utils.py:</strong> Helper utilities (password hashing, token generation, filename sanitizing).</li>
  <li><strong>data/users.json:</strong> Stores users' SHA-256 password hashes and role assignments (admin, editor, viewer).</li>
  <li><strong>models/vectorstore.pkl:</strong> FAISS-based LLM search index for fast document retrieval.</li>
  <li><strong>web/app.py:</strong> Flask server — handles login, folder browsing, uploads, and search.</li>
  <li><strong>web/forms.py:</strong> User login form (username, password, 2FA token).</li>
  <li><strong>web/xforms.py:</strong> Upload document form, create folder form, and search query form.</li>
  <li><strong>web/templates/*.html:</strong> HTML templates for login, dashboard, folder listing, uploading, and searching documents.</li>
  <li><strong>web/static/style.css:</strong> Simple and professional CSS for styling the web interface.</li>
</ul>

<hr>

<h2>🛠 Step-by-Step Setup Instructions</h2>

<h3>1. Clone the Repository</h3>

<pre><code>git clone https://github.com/yourusername/secure_docvault.git
cd secure_docvault
</code></pre>

<h3>2. Make Setup Script Executable</h3>

<pre><code>chmod +x setup.sh
</code></pre>

<h3>3. Run the Setup Script</h3>

<pre><code>./setup.sh
</code></pre>

<p>This will:</p>
<ul>
  <li>Update your system packages</li>
  <li>Install Python3, pip, venv, and required libraries</li>
  <li>Create a virtual environment <code>venv/</code> and activate it</li>
  <li>Install Python libraries listed in <code>requirements.txt</code></li>
  <li>Create necessary directories <code>data/vault</code> and <code>models/</code></li>
  <li>Generate a 32-byte AES encryption key and TOTP secret</li>
  <li>Create an initial <code>admin</code> user (username: admin, password: admin123)</li>
</ul>

<h3>4. (Optional) Customize Configuration</h3>

<p>Edit <code>config/settings.py</code> to customize:</p>
<ul>
  <li>Flask secret key</li>
  <li>Encryption key</li>
  <li>2FA seed</li>
  <li>Role definitions</li>
</ul>

<h3>5. Build Initial Vectorstore for Semantic Search</h3>

<p>After uploading or placing documents into <code>data/vault/</code>:</p>

<pre><code>source venv/bin/activate
python3 core/build_vectorstore.py
</code></pre>

<p>This will create <code>models/vectorstore.pkl</code>.</p>

<h3>6. Start the Web Server</h3>

<pre><code>source venv/bin/activate
python3 web/app.py
</code></pre>

<h3>7. Access the Web Interface</h3>

<p>Open your browser:</p>

<pre><code>http://localhost:5000
</code></pre>

✅ Login with:
<ul>
  <li>Username: <code>admin</code></li>
  <li>Password: <code>admin123</code></li>
  <li>2FA Token: Generated from TOTP seed (can integrate with Google Authenticator or similar apps)</li>
</ul>

<hr>

<h2>🛡️ Security Notes</h2>

<ul>
  <li>Immediately change the default <code>admin</code> password after first login.</li>
  <li>Update the TOTP seed per user in production deployments.</li>
  <li>Secure <code>config/settings.py</code> and use environment variables for encryption keys if possible.</li>
</ul>

<hr>

<h2>📈 Future Improvements</h2>

<ul>
  <li>Admin dashboard for user management</li>
  <li>Automatic re-indexing when documents are uploaded</li>
  <li>Password reset and email verification system</li>
  <li>Document activity logging and auditing</li>
  <li>Encrypted backups and scheduled snapshot exports</li>
</ul>

<hr>

<h2>📜 License</h2>

<p>MIT License — Open source and open to contributions!</p>

<hr>

<h2>👨‍💻 Author</h2>

<ul>
  <li><a href="https://github.com/yourusername">Your Name</a> — AI Engineer & Cybersecurity SME</li>
</ul>

</body>
</html>
