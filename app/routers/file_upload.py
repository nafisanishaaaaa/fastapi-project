from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form


router = APIRouter()


@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File()):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }

@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {
        "file_size": len(file)
    }
#Multiple File Uploads
@router.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {
        "filenames": [
            file.filename for file in files
        ]
    }

# Request Forms and Files
@router.post("/files-form/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }