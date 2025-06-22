# AI Image Sorter

A desktop application built with **PyQt5** for automatically sorting images into categories using a machine learning model. Images can be added via drag and drop, and the application displays the current image while allowing users to sort all images with one click.

---

## Features

- 🖼️ **Drag & Drop Interface** – Easily add images to the app by dropping them into the window.
- 📸 **Live Preview** – View the current image being processed.
- 🧠 **AI-Powered Sorting** – Automatically classifies and sorts images into folders based on predicted categories.
- 📁 **Organized Output** – Sorted images are stored in `assets/sorted/<category>` directories.

---

## Requirements

- Python 3.7+
- PyQt5
- PyTorch
- Torchvision
- PIL

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-image-sorter.git
   cd ai-image-sorter
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

---

## Project Structure

.  
├── assets/  
│   ├── dataset/           # Images used to fine-tune pre-trained model
│   ├── test_images/       # Temporarily stored input images  
│   └── sorted/            # Output folder for sorted images  
├── src/  
│   ├── AI_trainer.py      # File used to fine-tune pre-trained model
│   ├── main_window.py     # Main PyQt5 window class  
│   ├── image_view.py      # Image preview widget  
│   └── sorter.py          # AI sorting logic (model-based predictions)  
├── run.py                 # Entry point to start the app  
└── README.md              # Project documentation  

---

## Usage

0. If you want to fine tune the model to your needs you need to launch AI_trainer.py with your images in dataset/folders (folder names determine the category of images)
1. Start the application with `python run.py`.  
2. Drag and drop image files into the main window.  
3. Click "Sort Images" to classify them.  
4. The application will:  
   - Predict categories for each image  
   - Sort them into appropriately named folders in `assets/sorted/`  
   - Update the interface with feedback  

---

## Notes

- The accuracy and behavior of the sorter depend on your implementation of `Sorter.predict(image_path)` in `src/sorter.py`.  
- This project is designed with modularity in mind – models, logic, and UI components are separated for ease of future updates or enhancements.  


## Future Plans

Although no immediate expansions are planned, the architecture allows for potential improvements such as:

- Model training from within the app  
- Batch editing or undo functionality  
- Integration with cloud storage (e.g., Google Drive, Dropbox)  
- Custom user-trained categories  

---

## Author

Developed by Cezary Kochański
Feel free to fork or contribute!
