from app import db


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    spirit = db.Column(db.String)
    flavor = db.Column(db.String)
    bottle = db.Column(db.String)
    quantity = db.Column(db.Integer)
    email = db.Column(db.String)
    label = db.relationship("Label", back_populates="item")


    def to_dict(self, label=True):
        item_as_dict = {
            "id": self.item_id, 
            "spirit": self.spirit, 
            "flavor": self.flavor, 
            "bottle": self.bottle, 
            "quantity": self.quantity,
            "email": self.email
            }
        if label:
            item_as_dict["label"] = [label.to_dict() for label in self.label]

        return item_as_dict


    @classmethod
    def from_dict(cls, item_data):
        new_item = cls(
            spirit=item_data["spirit"],
            flavor=item_data["flavor"],
            bottle=item_data["bottle"],
            quantity=item_data["quantity"],
            email=item_data["email"],
        )

        return new_item