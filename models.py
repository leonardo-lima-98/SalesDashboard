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
    state_abbr = Column(String(5), nullable=False)
    created_at = Column(String(30), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "birthday": str(self.birthday),
            "country": self.country,
            "state": self.state,
            "created_at": str(self.created_at),
        }

class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    value = Column(DECIMAL(8, 2), nullable=False)
    on_offer = Column(Boolean, nullable=False)
    offer_percent = Column(DECIMAL(8, 2), nullable=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value": float(self.value),
            "on_offer": self.on_offer,
            "offer_percent": float(self.offer_percent) if self.offer_percent else None,
        }

class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"), nullable=False)
    purchase_date = Column(Date, nullable=False)
    purchase_value = Column(DECIMAL(8, 2), nullable=False)
    coupon_used = Column(Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "customer_id": str(self.customer_id),
            "product_id": str(self.product_id),
            "purchase_date": str(self.purchase_date),
            "purchase_value": float(self.purchase_value),
            "coupon_used": self.coupon_used,
        }
    
    def __repr__(self):
        return (
            f"<Purchase(id={self.id}, customer_id={self.customer_id}, "
            f"product_id={self.product_id}, purchase_value={self.purchase_value}, "
            f"coupon_used={self.coupon_used})>"
        )
