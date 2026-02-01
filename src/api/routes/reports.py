from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
import os

from src.services.report_generator import (
    generate_json_report,
    generate_pdf_report
)

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/download")
def download_report(format: str = Query(..., description="json ou pdf")):
    format = format.lower()

    if format == "json":
        file_path = generate_json_report()
        return FileResponse(
            file_path,
            media_type="application/json",
            filename="report.json"
        )

    elif format == "pdf":
        file_path = generate_pdf_report()
        return FileResponse(
            file_path,
            media_type="application/pdf",
            filename="report.pdf"
        )

    else:
        raise HTTPException(
            status_code=400,
            detail="Formato inválido. Use 'json' ou 'pdf'."
        )

print("🚀 reports router carregado")

