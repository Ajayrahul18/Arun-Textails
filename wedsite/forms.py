
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, NumberRange
from flask_wtf.file import FileField, FileRequired





class ShopItemsForm(FlaskForm):
    choices = [('all', 'All Products'), ('kids', 'Kids'), ('boys', 'Boys'), ('girls', 'Girls'), ('men', 'Men'), ('women', 'Woman')]
    product_name = StringField('Name of Product', validators=[DataRequired()])
    current_price = FloatField('Current Price', validators=[DataRequired()])
    previous_price = FloatField('Previous Price', validators=[DataRequired()])
    product_picture = FileField('Product Picture', validators=[DataRequired()])
    product_tag = SelectField('Product Filter', choices=choices, default='all')

    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update')

class InstaForm(FlaskForm):
    product_picture = FileField('Product Picture', validators=[DataRequired()])
    
    add_product = SubmitField('Add Product')



