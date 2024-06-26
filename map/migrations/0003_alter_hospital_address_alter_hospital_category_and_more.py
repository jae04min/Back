
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_hospital_address_alter_hospital_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.CharField(default='Comment', max_length=30),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='category',
            field=models.CharField(default='Comment', max_length=10),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='latitude',
            field=models.FloatField(default='Comment'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='longitude',
            field=models.FloatField(default='Comment'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='place_name',
            field=models.CharField(default='Comment', max_length=30),
        ),
    ]
