# Generated by Django 4.1.3 on 2022-11-18 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('S', 'Small 34-37'), ('M', 'Medium 38-40'), ('L', 'Large 41-43'), ('XL', 'XL 44-46'), ('XXL', 'XXL 47-50')], max_length=100)),
                ('s_type', models.CharField(choices=[('T', 'T-Shirts'), ('H', 'Hoodie'), ('F', 'Featured')], max_length=100)),
                ('cost', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('room_no', models.IntegerField(default=None)),
                ('hostel', models.CharField(choices=[('SI', 'SIANG'), ('LO', 'LOHIT'), ('DH', 'DIHING'), ('DI', 'DISANG'), ('SS', 'SUBHANSRI'), ('DS', 'DHANSRI'), ('BH', 'BHRAHMAPUTRA'), ('KM', 'KAMENG'), ('BA', 'BARAK'), ('UM', 'UMIAM'), ('MA', 'MANAS'), ('KA', 'KAPILI')], max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('merch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.merch')),
            ],
        ),
    ]
