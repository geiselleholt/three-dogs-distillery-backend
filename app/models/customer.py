from app import db


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default = False)
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)
    order = db.relationship("Order", back_populates="customer")

    def to_dict(self):
        customer_as_dict = {
            "id": self.customer_id,
            "user_name": self.user_name,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address
            }            

        return customer_as_dict

    @classmethod
    def from_dict(cls, customer_data):
        new_customer = cls(
            user_name=customer_data["user_name"],
            password=customer_data["password"],
            first_name=customer_data["first_name"],
            last_name=customer_data["last_name"],
            email=customer_data["email"],
            phone_number=customer_data["phone_number"],
            address=customer_data["address"]
        )

        return new_customer
