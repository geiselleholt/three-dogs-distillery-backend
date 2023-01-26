from app import db


class Label(db.Model):
    label_id = db.Column(db.Integer, primary_key=True)
    font = db.Column(db.Integer)
    name = db.Column(db.Integer)
    message = db.Column(db.String)
    image = db.Column(db.LargeBinary)
    item_id = db.Column(db.Integer, db.ForeignKey("item.item_id"))
    item = db.relationship("Item", back_populates="label")

    def to_dict(self):
        return dict(
            id=self.label_id,
            font=self.font,
            name=self.name,
            message=self.message,
            image=self.image,
            item_id=self.item_id
        )

    @classmethod
    def from_dict(cls, label_data):
        new_label = cls(
            font=label_data["font"],
            name=label_data["name"],
            message=label_data["message"],
            image=label_data["image"],
            item_id=label_data["item_id"]
        )

        return new_label