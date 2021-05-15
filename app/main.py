from fastapi import FastAPI


from routers import task

app = FastAPI()


@app.get("/")
# This is the main route of http://host/
async def root_route():
    return {"message": "This is the main route"}


app.include_router(task.router)
