import uvicorn

def start():
    uvicorn.run("Aplication.APiTest:app", 
                host="127.0.0.1", 
                port=8030, 
                reload=True
                )
    
if __name__ == "__main__":
    start()