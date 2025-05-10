import uvicorn


if __name__ == "__main__":
    uvicorn.run('agents:app', host="0.0.0.0", port=9363)