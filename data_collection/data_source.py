from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:@127.0.0.1/indian_pincode')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class IndianPinCode(Base):
    __tablename__ = 'indian_pincode'

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    office_name = Column(Text, name="office_name")
    pin_code = Column(Integer, index=True, name="pin_code")
    office_type = Column(String(10), name="office_type")
    delivery_status = Column(String(100), name="delivery_status")
    division_name = Column(Text, name="division_name")
    region_name = Column(Text, name="region_name")
    circle_name = Column(Text, name="circle_name")
    taluk = Column(Text, name="taluk")
    district_name = Column(Text, name="district_name")
    state_name = Column(Text, name="state_name")

    def __repr__(self):
        return "<IndianPinCode(pin_code='%s', office_name='%s', district_name='%s', state_name='%s')>" % (
            self.pin_code, self.office_name, self.district_name, self.state_name)


Base.metadata.create_all(engine)
