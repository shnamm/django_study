# Generated by Django 4.0.3 on 2023-02-04 03:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('coupon_name', models.CharField(max_length=100, unique=True)),
                ('coupon_type', models.CharField(choices=[('percentage', '정률'), ('fixed', '정액')], max_length=10)),
                ('discount_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0.5)])),
                ('discount_amount', models.PositiveIntegerField()),
                ('minimum_amount', models.FloatField()),
                ('is_issued', models.BooleanField(default=False)),
                ('is_used', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
