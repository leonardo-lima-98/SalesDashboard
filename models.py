from sqlalchemy import Column, String, Date, DECIMAL, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

import uuid

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    birthday = Column(Date, nullable=False)
    country = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)

class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    value = Column(DECIMAL(8, 2), nullable=False)
    on_offer = Column(Boolean, nullable=False)
    offer_percent = Column(DECIMAL(8, 2), nullable=True)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', value={self.value})>"

class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"), nullable=False)
    purchase_date = Column(Date, nullable=False)
    purchase_value = Column(DECIMAL(8, 2), nullable=False)
    coupon_used = Column(Boolean, nullable=False)
