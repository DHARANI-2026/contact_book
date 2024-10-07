# contact_book
Contact Book Application
A Contact Book built using Python and Tkinter, designed for managing personal or professional contact details. The app allows users to add, search, edit, and delete contacts, with an option to include profile photos.

Features
Add, Edit, Delete Contacts: Manage contact details including name, phone number, email, and address.
Profile Photo: Add a profile photo for each contact.
Search Contacts: Search contacts by name or phone number.
Display Contacts: View saved contacts with their details and profile photos.
Clean and Simple UI: User-friendly graphical interface with buttons aligned for easy access.
Technologies Used
Python: Core language for the application.
Tkinter: Used for building the graphical user interface (GUI).
Pillow (PIL): For handling and displaying profile images.
Installation
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/your-username/contact-book-app.git
Step 2: Navigate to the Project Directory
bash
Copy code
cd contact-book-app
Step 3: Install Dependencies
Ensure you have Tkinter and Pillow installed:

bash
Copy code
pip install pillow
Step 4: Run the Application
bash
Copy code
python contact_book.py
Usage
Add a Contact:

Enter the contact details (Name, Phone, Email, Address).
Optionally, click on Add Profile Photo to attach a profile picture.
Click Add Contact to save the contact.
Search for a Contact:

Enter the Name or Phone number in the respective fields and click Search Contact.
Edit or Delete a Contact:

Enter the Name of the contact you wish to modify or remove.
Click Edit Contact to update the contact's details.
Click Delete Contact to remove the contact.
View Contacts:

All saved contacts are displayed below, with their profile photos if available.
Project Structure
bash
Copy code
contact-book-app/
│
├── contact_book.py      # Main application code
├── contact.png          # Example logo image
├── README.md            # Project readme file
└── images/              # Directory for contact profile photos (optional)
Screenshots
Contact book with options to add, edit, delete, and search contacts.

Requirements
Python 3.x
Tkinter (usually included with Python)
Pillow (for handling images)
