from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine


class Customers(Base):  # Class para criar a tabela com o SQLAlchemy
    __tablename__ = "customers"  # Nome da Tabela
    id = Column(String, primary_key=True, index=False)  # Nome e informações da coluna.
    name = Column(String)  # Nome e informações da coluna.

    # Fazendo um relacionamento entre as tabelas
    orders = relationship("Orders", back_populates="customer")


class Orders(Base):  # Class para criar a tabela com o SQLAlchemy
    __tablename__ = "orders"  # Nome da Tabela
    id = Column(
        String, primary_key=True, index=False
    )  # Nome e informações da coluna (String e Primary Key)
    customer_id = Column(
        String, ForeignKey("customers.id")
    )  # Nome e informações da coluna (String)
    orderet_at = Column(DateTime)  # Nome e informações da coluna (DateTime)
    store_id = Column(
        String, ForeignKey("stores.id")
    )  # Nome e informações da coluna  (String)
    sub_total = Column(Integer)  # Nome e informações da coluna (Integer)
    tax_paid = Column(Integer)  # Nome e informações da coluna (Integer)
    order_total = Column(Integer)  # Nome e informações da coluna (Integer)

    customer = relationship(
        "Customers", back_populates="orders"
    )  # Fazendo um relacionamento entre as tabelas
    items = relationship("Items", back_populates="orders")
    stores = relationship("Stores", back_populates="orders")


class Items(Base):
    __tablename__ = "items"
    id = Column(
        String, primary_key=True, index=False
    )  # Nome e informações da coluna (String e Primary Key)
    order_id = Column(
        String, ForeignKey("orders.id")
    )  # Nome e informações da coluna (String)
    sku = Column(
        String, ForeignKey("products.sku")
    )  # Nome e informações da coluna (String)

    orders = relationship("Orders", back_populates="items")
    products = relationship("Products", back_populates="items")


class Products(Base):
    __tablename__ = "products"
    sku = Column(
        String, primary_key=True, index=False
    )  # Nome e informações da coluna (String e Primary Key)
    name = Column(String)  # Nome e informações da coluna (String)
    price = Column(Integer)  # Nome e informações da coluna (Integer)
    description = Column(String)  # Nome e informações da coluna (String)

    supplies = relationship("Supplies", back_populates="products")
    items = relationship("Items", back_populates="products")


class Stores(Base):
    __tablename__ = "stores"
    id = Column(
        String, primary_key=True, index=False
    )  # Nome e informações da coluna (String e Primary Key)
    opened_at = Column(DateTime)  # Nome e informações da coluna (DateTime)
    tax_rate = Column(Float)  # Nome e informações da coluna (Float)

    orders = relationship("Orders", back_populates="stores")


class Supplies(Base):
    __tablename__ = "supplies"
    id = Column(String, primary_key=True, index=False)
    name = Column(String)  # Nome e informações da coluna (String)
    cost = Column(Integer)  # Nome e informações da coluna (Integer)
    perishable = Column(String)  # Nome e informações da coluna (String)
    sku = Column(
        String, ForeignKey("products.sku")
    )  # Nome e informações da coluna (String)

    products = relationship("Products", back_populates="supplies")


Base.metadata.create_all(engine)
