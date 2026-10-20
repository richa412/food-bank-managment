from fastapi import  Depends ,FastAPI
from models import Product
from database import session ,engine 
import database_models
from sqlalchemy.orm import Session
app = FastAPI()
database_models.Base.metadata.create_all(bind = engine)
@app.get("/")
def greet():
    return" welcome to app"
products =[
    Product(id =1,name ="phone",description ="budget phone", price =99, quantity =10),
    Product(id =2,name ="laptop",description ="budgeting phone", price =999, quantity =11)]
def get_db():
    db = session()
    try:
      yield db 
    # waiting for others to use it 
    finally:
      db.close()

def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0:
       for product in products:
           db.add(database_models.Product(**product.model_dump()))
       db.commit()    
init_db()        
@app.get("/products")
def get_allproducts(db:Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()

    
    return db_products
@app.get("/product/{id}")
def get_product_by_id (id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id ==id).first()
    if db_product:
        return db_product
    return "product not found"
@app.post("/product")
def add_product(product:Product,db:Session =Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
@app.put("/product")
def update_product(id:int,product: Product, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id ==id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return"Product Updated"
    else:
         return "no product found"
@app.delete("/product")
def delete_product(id:int, db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id ==id).first()
    if db_product:
            db.delete(db_product)
            db.commit()
            return "product deleted"
    else:
        return "Product not found"    
        
        

          
            


 
