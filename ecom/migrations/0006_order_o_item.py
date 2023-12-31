# Generated by Django 4.2.6 on 2023-12-10 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pendding', 'pendding'), ('confirm', 'confirm'), ('cansal', 'cansal'), ('delevered', 'delevered')], default='pendding', max_length=9)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='o_item',
            fields=[
                ('otid', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('sub_total', models.BigIntegerField()),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.order')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.product')),
            ],
        ),
    ]
