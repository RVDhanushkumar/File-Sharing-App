# File Sharing App

This is a simple file sharing application built using Python and Tkinter. It allows users to start an FTP server, upload files to the server, and download files from the server.

## Features

- Start and stop an FTP server
- Select multiple files for upload
- Upload files to the server
- Refresh the file list
- Download files from the server

## Requirements

- Python
- tkinter (usually included in Python installations)
- pyftpdlib

## Usage

1. Run the `FileSharing.py` script.
2. Enter the server IP address and port number.
3. Click on "Start Server" to start the FTP server.
4. Use the "Select Files" button to select files for upload.
5. Click on "Upload Files" to upload the selected files to the server.
6. Use the "Refresh List" button to refresh the file list.
7. Click on "Download File" to download a selected file from the server.

## Note

- The uploaded files are stored in the `uploads` directory.
- The downloaded files are saved in the `downloads` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
