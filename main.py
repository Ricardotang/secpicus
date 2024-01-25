from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
import json
import uvicorn
from manager import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
info_map = load_all_info()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/manager", response_class=HTMLResponse)
async def get_manager(request: Request, manager_name: str):
    is_dict = isinstance(info_map, dict)
    print(is_dict)
    manager_info = get_manager_info(manager_name=manager_name, info_map=info_map)
    if manager_info is None:
        raise HTTPException(status_code=404, detail="Manager not found")

    return templates.TemplateResponse("manager.html", {
        "request": request, 
        "base_info": manager_info['base_info'],
        "total_value_img": "static/baillie/total_value_img.png",
        "top_10_img": manager_info["top_10_img"],
        "top_10_table": manager_info["top_10_table"],
        "gics_img": manager_info["gics_img"],
        "gics_table": manager_info["gics_table"],
        "percent_img": manager_info["percent_img"],
        "top5_issuer_img": manager_info["top5_issuer_img"],
        "top5_issuer_table": manager_info["top5_issuer_table"], 
        })


@app.get("/{id}.html", response_class=HTMLResponse)
async def get_manager(request: Request, id: str):

    manager_info = get_manager_by_id(id=id, info_map=info_map)
    if manager_info is None:
        raise HTTPException(status_code=404, detail="Manager not found")

    return templates.TemplateResponse("manager.html", {
        "request": request, 
        "base_info": manager_info['base_info'],
        "total_value_img": manager_info["total_value_img"],
        "top_10_img": manager_info["top_10_img"],
        # "top_10_table": manager_info["top_10_table"],
        "gics_img": manager_info["gics_img"],
        # "gics_table": manager_info["gics_table"],
        "percent_img": manager_info["percent_img"],
        "top5_issuer_img": manager_info["top5_issuer_img"],
        # "top5_issuer_table": manager_info["top5_issuer_table"], 
        })



if __name__ == "__main__":
    
    uvicorn.run("main:app", port=8000,  reload=True, log_level="info")