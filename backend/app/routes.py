from fastapi import APIRouter
router = APIRouter()
@router.get("/health")
def health_check():
    return {"status": "healthy"}


@router.get("/hello")
def hello(name: str = "World"):
    return {
        "message": f"Hello, {name}!"
    }


@router.get("/calculate-age")
def calculate_age(year_of_birth: int):
    from datetime import datetime

    current_year = datetime.now().year
    age = current_year - year_of_birth

    return {
        "year_of_birth": year_of_birth,
        "age": age
    }