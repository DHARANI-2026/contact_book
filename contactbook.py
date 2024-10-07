import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os

# Define a Contact class to store contact details
class Contact:
    def __init__(self, name, phone, email, address, photo_path=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.photo_path = photo_path

class ContactBookApp:---
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Styling
        root.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Logo
        logo = Image.open("E:/contact.png")
        logo = logo.resize((100, 100), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo)
        tk.Label(self.root, image=self.logo_img, bg="#f0f0f0").grid(row=0, column=0, columnspan=4, pady=10)

        # Input fields
        tk.Label(self.root, text="Name:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=3)

        tk.Label(self.root, text="Phone:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self.root, width=30)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=3)

        tk.Label(self.root, text="Email:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5, columnspan=3)

        tk.Label(self.root, text="Address:", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.root, width=30)
        self.address_entry.grid(row=4, column=1, padx=10, pady=5, columnspan=3)

        self.add_photo_btn = tk.Button(self.root, text="Add Profile Photo", command=self.add_photo, bg="#d1e7dd", relief="flat")
        self.add_photo_btn.grid(row=5, column=0, columnspan=4, pady=5)

        # Buttons
        button_style = {"bg": "#0d6efd", "fg": "white", "relief": "flat"}
        tk.Button(self.root, text="Add Contact", command=self.add_contact, **button_style).grid(row=6, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Edit Contact", command=self.edit_contact, **button_style).grid(row=6, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact, **button_style).grid(row=6, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact, **button_style).grid(row=6, column=3, padx=10, pady=10)

        # Display contacts section
        tk.Label(self.root, text="Saved Contacts:", bg="#f0f0f0", font=("Arial", 12, "bold")).grid(row=7, column=0, columnspan=4, padx=10, pady=10)
        self.contacts_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.contacts_frame.grid(row=8, column=0, columnspan=4)

    def add_photo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.photo_path = file_path

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone or not email or not address:
            messagebox.showerror("Error", "All fields are required.")
            return

        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists.")
            return

        self.contacts[name] = Contact(name, phone, email, address, self.photo_path)
        self.display_contacts()
        self.clear_entries()

    def edit_contact(self):
        name = self.name_entry.get().strip()

        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        self.contacts[name].phone = phone
        self.contacts[name].email = email
        self.contacts[name].address = address
        if self.photo_path:
            self.contacts[name].photo_path = self.photo_path
        self.display_contacts()
        self.clear_entries()

    def delete_contact(self):
        name = self.name_entry.get().strip()

        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        del self.contacts[name]
        self.display_contacts()
        self.clear_entries()

    def search_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name and not phone:
            messagebox.showerror("Error", "Enter Name or Phone to search.")
            return

        results = []
        for contact in self.contacts.values():
            if contact.name == name or contact.phone == phone:
                results.append(contact)

        if not results:
            messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            result_text = "\n".join([f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}, Address: {c.address}" for c in results])
            messagebox.showinfo("Search Result", result_text)

    def display_contacts(self):
        for widget in self.contacts_frame.winfo_children():
            widget.destroy()

        row = 0
        for contact in self.contacts.values():
            contact_frame = tk.Frame(self.contacts_frame, bg="#f0f0f0")
            contact_frame.grid(row=row, column=0, padx=10, pady=5, sticky="w")

            if contact.photo_path and os.path.exists(contact.photo_path):
                photo = Image.open(contact.photo_path)
                photo = photo.resize((50, 50), Image.Resampling.LANCZOS)
                photo_img = ImageTk.PhotoImage(photo)
                photo_label = tk.Label(contact_frame, image=photo_img, bg="#f0f0f0")
                photo_label.image = photo_img  # Keep a reference to avoid garbage collection
                photo_label.grid(row=0, column=0, rowspan=3, padx=10, pady=5)

            name_label = tk.Label(contact_frame, text=f"Name: {contact.name}", bg="#f0f0f0")
            name_label.grid(row=0, column=1, sticky="w")

            phone_label = tk.Label(contact_frame, text=f"Phone: {contact.phone}", bg="#f0f0f0")
            phone_label.grid(row=1, column=1, sticky="w")

            email_label = tk.Label(contact_frame, text=f"Email: {contact.email}", bg="#f0f0f0")
            email_label.grid(row=2, column=1, sticky="w")

            address_label = tk.Label(contact_frame, text=f"Address: {contact.address}", bg="#f0f0f0")
            address_label.grid(row=3, column=1, sticky="w")

            row += 1

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.photo_path = None

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
