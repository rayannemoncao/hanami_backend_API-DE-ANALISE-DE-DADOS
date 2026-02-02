from fastapi import APIRouter, UploadFile, HTTPException
import os

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/",
    summary="Upload de arquivo",
    description="Recebe um arquivo CSV ou XLSX e armazena para processamento posterior.",
    responses={
        200: {
            "description": "Upload realizado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "status": "sucesso",
                        "arquivo": "dados.csv"
                    }
                }
            }
        },
        400: {
            "description": "Arquivo inválido ou ausente"
        }
    })

async def upload_arquivo(file: UploadFile):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Arquivo não enviado.")

    extensao = os.path.splitext(file.filename)[1].lower()
    if extensao not in [".csv", ".xlsx"]:
        raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado.")

    path = os.path.join("src/runtime_data", file.filename)
    content = await file.read()
    with open(path, "wb") as f:
        f.write(content)

    return {"status": "sucesso", "arquivo": file.filename}
