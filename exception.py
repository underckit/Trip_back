from fastapi import HTTPException

def NotFound(x):
    if not x:
        raise HTTPException(status_code=404, detail="Item not found")
