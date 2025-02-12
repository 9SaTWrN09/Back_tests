import uvicorn
import os

def start():
    port = int(os.getenv("PORT", 8000))  # Usa el puerto que asigna Railway o 8000 por defecto
    uvicorn.run("Aplication.APiTest:app", 
                host="0.0.0.0",  # Permite accesos externos
                port=port, 
                reload=True
                )

if __name__ == "__main__":
    start()

