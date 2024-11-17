import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content=''):
    with open(path, 'w') as f:
        f.write(content)

# Project structure
directories = [
    'frontend/css',
    'frontend/js',
    'frontend/assets',
    'backend/utils',
    'backend/models',
    'docs/presentation'
]

# Create directories
for directory in directories:
    create_directory(directory)

# Create frontend files
create_file('frontend/index.html', '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Easy Leets - Graph Analysis Tool</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <div id="app">
        <h1>Easy Leets</h1>
        <div class="upload-container">
            <div class="drop-zone">
                <span class="drop-zone__prompt">Drop file here or click to upload</span>
                <input type="file" name="graphImage" class="drop-zone__input">
            </div>
        </div>
        <div id="result" class="result-container"></div>
    </div>
    <script src="js/main.js"></script>
</body>
</html>
''')

create_file('frontend/css/styles.css', '''
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background: #f5f5f5;
}

#app {
    max-width: 800px;
    margin: 0 auto;
}

.upload-container {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.drop-zone {
    max-width: 100%;
    height: 200px;
    padding: 25px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    cursor: pointer;
    border: 4px dashed #009578;
    border-radius: 10px;
}

.drop-zone--over {
    border-style: solid;
}

.drop-zone__input {
    display: none;
}

.result-container {
    margin-top: 20px;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
''')

create_file('frontend/js/main.js', '''
document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
    const dropZoneElement = inputElement.closest(".drop-zone");

    dropZoneElement.addEventListener("click", (e) => {
        inputElement.click();
    });

    inputElement.addEventListener("change", (e) => {
        if (inputElement.files.length) {
            updateThumbnail(dropZoneElement, inputElement.files[0]);
        }
    });

    dropZoneElement.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropZoneElement.classList.add("drop-zone--over");
    });

    ["dragleave", "dragend"].forEach((type) => {
        dropZoneElement.addEventListener(type, (e) => {
            dropZoneElement.classList.remove("drop-zone--over");
        });
    });

    dropZoneElement.addEventListener("drop", (e) => {
        e.preventDefault();

        if (e.dataTransfer.files.length) {
            inputElement.files = e.dataTransfer.files;
            updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
        }

        dropZoneElement.classList.remove("drop-zone--over");
    });
});

function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

    if (dropZoneElement.querySelector(".drop-zone__prompt")) {
        dropZoneElement.querySelector(".drop-zone__prompt").remove();
    }

    if (!thumbnailElement) {
        thumbnailElement = document.createElement("div");
        thumbnailElement.classList.add("drop-zone__thumb");
        dropZoneElement.appendChild(thumbnailElement);
    }

    thumbnailElement.dataset.label = file.name;

    if (file.type.startsWith("image/")) {
        const reader = new FileReader();

        reader.readAsDataURL(file);
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
        };
    }
}
''')

# Create backend files
create_file('backend/app.py', '''
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
''')

create_file('backend/requirements.txt', '''
fastapi==0.104.1
uvicorn==0.24.0
python-multipart==0.0.6
pillow==10.1.0
numpy==1.26.2
pydantic==2.5.2
python-dotenv==1.0.0
''')

# Create gitignore
create_file('.gitignore', '''
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Project specific
config.local.py
*.log
uploads/
''')

# Update README.md
create_file('README.md', '''
# Easy Leets

AI-powered graph problem solver that converts graph images into working solutions.

## Features

- Drag & Drop Image Upload
- Real-time Image Preview
- Graph Analysis using Vision AI
- Automated Code Generation
- Terminal-style Code Display
- Copy-to-Clipboard Functionality

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Atharva2099/Easy-Leets.git
   cd Easy-Leets
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. Run the application:
   ```bash
   python backend/app.py
   ```

## Technology Stack

- Frontend: HTML5, CSS3, Vanilla JavaScript
- Backend: FastAPI (Python)
- AI: Vision AI for graph analysis

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
''')

print("Project structure created successfully!")