from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse, FileResponse
import cv2
import numpy as np
import uuid 
from utils import get_function

app = FastAPI(title="MCP API", version="1.0.0")


@app.post("/process_image/")
async def process_image(
    file: UploadFile = File(...),
    prompt: str = Form(...),
):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Select function based on prompt
    func = get_function(prompt)
    if not func:
        return JSONResponse(status_code=400, content={"error": "Invalid prompt"})
    
    # Apply edit
    output =  func(img)
    
    # Save to temp file
    out_path = f"static/{uuid.uuid4().hex}.jpg"
    cv2.imwrite(out_path, output)
    
    return FileResponse(out_path, media_type="image/jpeg")