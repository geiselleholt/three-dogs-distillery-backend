from app import db


class Label(db.Model):
    label_id = db.Column(db.Integer, primary_key=True)
    name_font = db.Column(db.String)
    message_font = db.Column(db.String)
    name_font_color = db.Column(db.String)
    message_font_color = db.Column(db.String)
    name = db.Column(db.String)
    message = db.Column(db.String)
    image = db.Column(db.String)
    background_color = db.Column(db.String)
    item_id = db.Column(db.Integer, db.ForeignKey("item.item_id"))
    item = db.relationship("Item", back_populates="label")

    def to_dict(self):
        return dict(
            id=self.label_id,
            name=self.name,
            name_font=self.name_font,
            name_font_color=self.name_font_color,
            message=self.message,
            message_font=self.message_font,
            message_font_color=self.message_font_color,
            image=self.image,
            background_color=self.background_color,
            item_id=self.item_id
        )

    @classmethod
    def from_dict(cls, label_data):
        new_label = cls(
            name=label_data["name"],
            name_font=label_data["name_font"],
            name_font_color=label_data["name_font_color"],
            message=label_data["message"],
            message_font=label_data["message_font"],
            message_font_color=label_data["message_font_color"],
            image=label_data["image"],
            background_color=label_data["background_color"],
            item_id=label_data["item_id"]
        )

        return new_label