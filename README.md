# -Wake-On-Lan-Python-Remote-from-everywhere-
This script enables you to conveniently and securely wake up your devices at home while you are away, without requiring any prior software installation. It is developed in Python 3.

# What You Need

- **An Online Email IMAP Account**
  - This type of email account allows you to access and manage your emails from multiple devices while keeping them synchronized. IMAP stands for Internet Message Access Protocol, which enables you to read your emails without downloading them to a single device.

- **Device Settings**
  - Ensure that Wake-on-LAN (WoL) is enabled on the devices you wish to power on remotely.
  - If Wake-on-LAN is not enabled, access the BIOS settings of each device and turn on the feature.

## Setup Instructions for Remote Power-On Script

1. **Script Execution:**
   - Ensure the script is executed on a primary computer within your local network.
   - Options for Execution:
     - Use a virtual machine or container for isolation.
     - Convert the Python script into an executable (EXE) file for workstations without Python installed.

---

## How It Works: Remote Power-On Process

This script enables you to remotely power on computers within your local network using just an email. Follow these steps:

1. **Installation:**
   - Install the script on a designated computer within your home network.

2. **Sending the Wake-Up Email:**
   - Identify the computer you wish to power on by its name.
   - Compose an email with the subject line containing the computer name:
     ```
     Subject: <Computer_Name>
     ```
   - Send this email to your designated mailbox that the script monitors.

3. **Automatic Email Monitoring:**
   - The script continuously checks your mailbox for incoming emails.
   - Upon receiving an email, it extracts the computer name from the subject line.

4. **IP Address and MAC Address Retrieval:**
   - The script locates the corresponding **IP address** and **MAC address** for the identified computer within your network.

5. **Magic Packet Transmission:**
   - Utilizing the MAC address, the script sends a "Magic Packet" to wake the corresponding computer.

---

## Future Development:
- The script can retain the IP address for potential enhancements, such as enabling remote shutdown capabilities via SSH, providing a secure method for network control.

---

### Important Note:
Simply send an email with the correct subject format, and the script will handle the remainder of the process automatically!
