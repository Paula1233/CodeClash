from ..base import db


class Problem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    tests = db.relationship('ProblemTest')

    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    difficulty = db.Column(db.Integer(), nullable=False)

    #def __init__(self):
    #    pass

    """@property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def difficulty(self):
        return self._difficulty"""
