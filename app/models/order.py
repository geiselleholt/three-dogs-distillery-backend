from app import db


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    sub_total = db.Column(db.Integer)
    total = db.Column(db.Integer)
    delivery_date = db.Column(db.String)
    status = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.customer_id"))
    customer = db.relationship("Customer", back_populates="orders")
    items = db.relationship("Item", back_populates="order")

    def to_dict(self, order_data):
        order_dict = dict(
            id=self.order_id,
            sub_total=self.sub_total,
            total=self.total,
            delivery_date=self.delivery_date,
            status=self.status,
        )

        if self.customer_id:
            order_dict["customer_id"] = self.customer_id
        
        return order_dict

    @classmethod
    def from_dict(cls, order_data):
        new_order = cls(
            sub_total=order_data["sub_total"],
            total=order_data["total"],
            delivery_date=order_data["delivery_date"],
            status=order_data["status"],
            customer_id=order_data["customer_id"]
        )

        return new_order
