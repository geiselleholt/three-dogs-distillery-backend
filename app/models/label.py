from app import db


class Label(db.Model):
    label_id = db.Column(db.Integer, primary_key=True)
    font = db.Column(db.String)
    name = db.Column(db.String)
    message = db.Column(db.String)
    item_id = db.Column(db.Integer, db.ForeignKey("item.item_id"))
    item = db.relationship("Item", back_populates="label")

    def to_dict(self):
        return dict(
            id=self.label_id,
            font=self.font,
            name=self.name,
            message=self.message,
            item_id=self.item_id
        )

    @classmethod
    def from_dict(cls, label_data):
        new_label = cls(
            font=label_data["font"],
            name=label_data["name"],
            message=label_data["message"],
            item_id=label_data["item_id"]
        )

        return new_label