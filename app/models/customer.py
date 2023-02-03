from app import db


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)
    orders = db.relationship("Order", back_populates="customer")

    def to_dict(self):
        customer_as_dict = {
            "id": self.customer_id,
            "is_admin": self.is_admin,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address
            }            

        return customer_as_dict

    @classmethod
    def from_dict(cls, customer_data):
        new_customer = cls(
            is_admin=customer_data["is_admin"],
            first_name=customer_data["first_name"],
            last_name=customer_data["last_name"],
            email=customer_data["email"],
            address=customer_data["address"]
        )


        return new_customer
