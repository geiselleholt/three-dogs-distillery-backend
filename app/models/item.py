from app import db


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    spirit_type = db.Column(db.String)
    spirit_flavor = db.Column(db.String)
    bottle_type = db.Column(db.String)
    bottle_quantity = db.Column(db.Integer)
    age_time = db.Column(db.String)
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"))
    order = db.relationship("Order", back_populates="items")
    label = db.relationship("Label", back_populates="item")

    def to_dict(self):
        return dict(
            id=self.item_id,
            spirit_type=self.spirit_type,
            spirit_flavor=self.spirit_flavor,
            bottle_type=self.bottle_type,
            bottle_quantity=self.bottle_quantity,
            age_time=self.age_time,
            order_id=self.order_id           
        )

    @classmethod
    def from_dict(cls, item_data):
        new_item = cls(
            spirit_type=item_data["spirit_type"],
            spirit_flavor=item_data["spirit_flavor"],
            bottle_type=item_data["bottle_type"],
            bottle_quantity=item_data["bottle_quantity"],
            age_time=item_data["age_time"],
            order_id=item_data["order_id"]
        )

        return new_item