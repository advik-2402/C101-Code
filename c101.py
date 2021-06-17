import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.Ay7mXcT_loWO0tu70iV7PjlIwKRXJKK-04E8NX2k8kwbxBKWfHwHWVGnXV1mNowWbgd3x6MUEhhUtNLijNeMykAFgnjYl-Wi4N2HmD3UF5Op7FSHzIOqZO030ke4j2fS7lOMxsE'
    transferData = TransferData(access_token)

    file_from = input("Enter File Path: ")
    # The full path to upload the file to, including the file name
    file_to = input("Enter File Destination: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved!")

main()
