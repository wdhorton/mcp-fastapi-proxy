from fastapi import FastAPI

app = FastAPI()


@app.get("/get_weather")
async def get_weather(zip_code: str):
    """
    Get the weather for a given location
    """
    return {"temperature": "20 degrees F"}