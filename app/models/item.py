from app import db


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    spirit = db.Column(db.String)
    flavor = db.Column(db.String)
    bottle = db.Column(db.String)
    quantity = db.Column(db.Integer)
    # order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"))
    # order = db.relationship("Order", back_populates="items")
    label = db.relationship("Label", back_populates="item")

    def to_dict(self):
        return dict(
            id=self.item_id,
            spirit=self.spirit,
            flavor=self.flavor,
            bottle=self.bottle,
            quantity=self.quantity,
            # order_id=self.order_id           
        )

    @classmethod
    def from_dict(cls, item_data):
        new_item = cls(
            spirit=item_data["spirit"],
            flavor=item_data["flavor"],
            bottle=item_data["bottle"],
            quantity=item_data["quantity"],
            # order_id=item_data["order_id"]
        )

        return new_item