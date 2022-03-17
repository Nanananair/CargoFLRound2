from email.mime import base
from typing import Text
from sqlalchemy import Column, Integer, String, DateTime, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.sql.sqltypes import Boolean

base = declarative_base()

class Shipment(base): 
    __tablename__ = 'shipments'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    docket = Column(Integer(9),nullable=False, unique= True)
    lsp_lr = Column(String(16))
    invoice = Column(Integer(9), nullable=False)
    pickup_date = Column(DateTime(timezone=True))
    edd = Column(DateTime(timezone=True))
    actual_delivery_date = Column(DateTime(timezone=True))
    consigner = Column(String(16))
    consignee = Column(String(16))
    from_city = Column(String(16))
    to_city = Column(String(16))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_on =  Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, docket, lsp_lr, invoice, pickup_date, edd,actual_delivery_date,  consigner, consignee, from_city, to_city  ) -> None:
        super().__init__()
        self.name = name
        self.mobile_no = mobile_no
        self.email = email
        self.employee_branch = employee_branch

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}