import os
from pyftpdlib.authorizers import DummyAuthorizer
from tkinter import Tk, Label, Button, filedialog, Listbox, Scrollbar, Entry, MULTIPLE
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from ftplib import FTP


UPLOAD_DIR = "uploads"
DOWNLOAD_DIR = "downloads"


def start_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(UPLOAD_DIR)
    handler = FTPHandler
    handler.authorizer = authorizer
    server_ip = server_ip_entry.get()
    server_port = int(server_port_entry.get())
    server = FTPServer((server_ip, server_port), handler)
    try:
        server.serve_forever()
        status_label.config(text=f"FTP server running on {server_ip}:{server_port}")
    except Exception as e:
        status_label.config(text=f"Failed to start FTP server: {e}")


def stop_ftp_server():
    status_label.config(text="FTP server stopped.")


def select_files():
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        files_listbox.insert('end', file_name)


def upload_files():
    selected_files = files_listbox.get(0, 'end')
    if selected_files:
        with FTP() as ftp:
            server_ip = server_ip_entry.get()
            server_port = int(server_port_entry.get())
            ftp.connect(server_ip, server_port)
            ftp.login()
            for file_path in selected_files:
                with open(file_path, "rb") as f:
                    ftp.storbinary("STOR " + os.path.basename(file_path), f)
            status_label.config(text="Files uploaded successfully")
            refresh_files_list()
    else:
        status_label.config(text="Please select files")


def refresh_files_list():
    files_listbox.delete(0, 'end')
    with FTP() as ftp:
        server_ip = server_ip_entry.get()
        server_port = int(server_port_entry.get())
        ftp.connect(server_ip, server_port)
        ftp.login()
        files = ftp.nlst()
        for file in files:
            files_listbox.insert('end', file)


def download_file():
    selected_file = files_listbox.get(files_listbox.curselection())
    download_dir = download_dir_label.cget("text")
    if selected_file and download_dir:
        with FTP() as ftp:
            server_ip = server_ip_entry.get()
            server_port = int(server_port_entry.get())
            ftp.connect(server_ip, server_port)
            ftp.login()
            with open(os.path.join(download_dir, selected_file), "wb") as f:
                ftp.retrbinary("RETR " + selected_file, f.write)
            status_label.config(text="File downloaded successfully")
    else:
        status_label.config(text="Please select a file and download directory")


root = Tk()
root.title("File Sharing App")

# Server
server_ip_label = Label(root, text="Server IP:")
server_ip_label.pack(pady=5)
server_ip_entry = Entry(root)
server_ip_entry.pack(pady=5)

server_port_label = Label(root, text="Server Port:")
server_port_label.pack(pady=5)
server_port_entry = Entry(root)
server_port_entry.pack(pady=5)

start_button = Button(root, text="Start Server", command=start_ftp_server)
start_button.pack(pady=10)

stop_button = Button(root, text="Stop Server", command=stop_ftp_server)
stop_button.pack(pady=10)

# Client
file_select_button = Button(root, text="Select Files", command=select_files)
file_select_button.pack(pady=10)

files_listbox = Listbox(root, height=5, width=50, selectmode=MULTIPLE)
files_listbox.pack(pady=10)

upload_button = Button(root, text="Upload Files", command=upload_files)
upload_button.pack(pady=10)

refresh_button = Button(root, text="Refresh List", command=refresh_files_list)
refresh_button.pack(pady=5)

download_button = Button(root, text="Download File", command=download_file)
download_button.pack(pady=10)

download_dir_label = Label(root, text="")
download_dir_label.pack(pady=10)

status_label = Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
