from fastapi import FastAPI


app = FastAPI(title="School Management System API")

@app.get("/")
async def health_check():
    return {"status": "healthy"}
