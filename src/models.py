from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Customers(Base):
    __tablename__ = "customers"
    id = Column(String, primary_key=True, index=False)
    name = Column(String)

    orders = relationship("Orders", back_populates="customer")


class Orders(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, index=False)
    customer = Column(String, ForeignKey("customers.id"))
    orderet_at = Column(DateTime)
    store_id = Column(String, ForeignKey("stores.id"))
    sub_total = Column(Integer)
    tax_paid = Column(Integer)
    order_total = Column(Integer)

    customer = relationship("Customers", back_populates="orders")

    items = relationship("Items", back_populates="orders")

    stores = relationship("Stores", back_populates="orders")


class Items(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True, index=False)
    order_id = Column(String, ForeignKey("orders.id"))
    sku = Column(String, ForeignKey("products.sku"))

    orders = relationship("Orders", back_populates="items")

    products = relationship("Products", back_populates="items")


class Products(Base):
    __tablename__ = "Products"
    sku = Column(String, primary_key=True, index=False)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)

    supplies = relationship("Supplies", back_populates="products")

    items = relationship("Items", back_populates="products")


class Stores(Base):
    __tablename__ = "stores"
    id = Column(String, primary_key=True, index=False)
    order_id = Column(String)
    opened_at = Column(DateTime)
    tax_rate = Column(float)

    orders = relationship("Orders", back_populates="stores")


class Supplies(Base):
    __tablename__ = "supplies"
    id = Column(String, primary_key=True, index=False)
    name = Column(String)
    cost = Column(Integer)
    perishable = Column(String)
    sku = Column(String, ForeignKey("products.sku"))

    products = relationship("Products", back_populates="supplies")
