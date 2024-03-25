# Generated by Django 5.0.3 on 2024-03-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review_stars_alter_review_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='product.tag'),
        ),
    ]