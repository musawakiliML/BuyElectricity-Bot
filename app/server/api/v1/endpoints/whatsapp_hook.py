from fastapi import FastAPI, APIRouter

router = APIRouter()


@router.get("/")
def buy_electricity_webhook(request: request):
    
    VERIFY_TOKEN = "useflushbot"

    return {"hello"}
    