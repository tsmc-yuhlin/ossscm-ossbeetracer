from fastapi import Body, FastAPI

app = FastAPI()


@app.post('/test')
async def update_item(
        payload: dict = Body(...)
):

    print(payload)
#    print(payload['operator'])
#    print(payload['event_data']['repository'])

## uvicorn test:app --reload --host 0.0.0.0
##import uvicorn
##if __name__ == '__main__' :
##    uvicorn.run(app, port=8080 , host='0.0.0.0')
