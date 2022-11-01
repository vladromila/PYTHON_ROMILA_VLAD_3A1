import os


def fileData(file):
    try:
        assert (os.path.isfile(file)), "Invalid Path!"
        return {"full_path": os.path.abspath(file),
                "file_size": os.path.getsize(file),
                "file_extension": file.split(".")[len(file.split("."))-1],
                "can_read": os.access(file, os.R_OK),
                "can_write": os.access(file, os.W_OK)}
    except Exception as e:
        return str(e)


print(fileData("./testfolder/test.txt"))
