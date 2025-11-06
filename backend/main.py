from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Ratatouille API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Главная страница"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/test")
def test_endpoint():
    return {"test": "Это тестовый эндпоинт"}

@app.get("/search/company/{inn}")
def search_company(inn: str):
    return {"inn": inn, "name": "Тестовая компания"}

@app.get("/search/individual/")
def search_individual(name: str = "Иванов"):
    return {"name": name, "status": "найден"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)