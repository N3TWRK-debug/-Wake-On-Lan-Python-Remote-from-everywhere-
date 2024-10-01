import imaplib
import email
from getmac import get_mac_address
import tkinter as tk
import time
from datetime import datetime

# Lists for storing MAC addresses and for hostnames for logging
mac_address_list = []
subject_list = []

def update_output(output_text, message):
    output_text.insert(tk.END, message + "\n")
    output_text.update()
    output_text.see(tk.END)

def function1(output_text):
    try:
        update_output(output_text, "The script is now starting ... Searching for emails")

        # Establish connection to the IMAP server with a timeout
        imap_server = imaplib.IMAP4_SSL("secureimap.example.com", timeout=5)  # Replace with a valid IMAP server
        imap_server.login("user@example.com", "your_password")  # Replace with valid email and password
        
        # Select the mailbox
        imap_server.select("INBOX")

        # Retrieve emails
        status, email_ids = imap_server.search(None, "ALL")

        # For each email
        for email_id in email_ids[0].split():
            status, email_data = imap_server.fetch(email_id, "(RFC822)")

            # Extract email content
            raw_email = email_data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Read only the subject of the email
            subject = msg["Subject"].strip()
            subject = subject.replace("Backup successfully completed", "").strip()

            update_output(output_text, subject)

            # Storing the names of the computers mentioned in the emails
            subject_list.append(subject)
            
            # To avoid loss of variables upon script termination, log today's date and information
            # Log file
            file_path = "C:\\Users\\YourUsername\\Desktop\\Log.txt"  # Replace with valid path

            def write_to_file(file_path, subject):
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(file_path, "a") as file:
                    file.write(f"{current_time}: {subject}\n")

            write_to_file(file_path, subject)

            # Determine the MAC address
            mac_address = get_mac_address(ip=subject)
            if mac_address is not None:
                update_output(output_text, mac_address)

                # Store the MAC address in the list, only if it is not None
                mac_address_list.append(mac_address)

            update_output(output_text, "Searching ...")
            time.sleep(5)

    except Exception as e:
        update_output(output_text, "Error executing the script: " + str(e))

def function2(output_text):
    if not mac_address_list:
        update_output(output_text, "There are no MAC addresses in the list")
    else:
        for mac_address in mac_address_list:
            update_output(output_text, mac_address)

def function3(output_text):
    if not subject_list:
        update_output(output_text, "No other computers have been shut down yet")
    else:
        update_output(output_text, str(subject_list) + "\nThese computers have already been shut down")

# Create the main window
root = tk.Tk()

# Create a textarea for output
output_text = tk.Text(root)
output_text.pack()

# Create buttons for the various functions
button1 = tk.Button(root, text="Start the script", command=lambda: function1(output_text))
button1.pack()

button2 = tk.Button(root, text="What MAC addresses are in the list for waking up", command=lambda: function2(output_text))
button2.pack()

button3 = tk.Button(root, text="Which computers have all been shut down", command=lambda: function3(output_text))
button3.pack()

# Start the GUI loop
root.mainloop()
