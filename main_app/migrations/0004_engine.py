# Generated by Django 4.1.1 on 2022-10-03 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(default='', max_length=100)),
                ('displacement', models.CharField(max_length=100)),
                ('induction', models.CharField(max_length=100)),
                ('configuration', models.CharField(max_length=100)),
                ('horsepower', models.CharField(max_length=100)),
                ('torque', models.CharField(max_length=100)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engine', to='main_app.car')),
            ],
        ),
    ]