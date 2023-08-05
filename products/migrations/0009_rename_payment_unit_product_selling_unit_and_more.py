# Generated by Django 4.2.4 on 2023-08-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_likes_number_like_card'),
        ('products', '0008_productreview_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='payment_unit',
            new_name='selling_unit',
        ),
        migrations.AlterField(
            model_name='product',
            name='delevery_range',
            field=models.CharField(choices=[('wilaya', 'wilaya'), ('baladiya', 'baladiya'), ('country', 'country'), ('no delevery', 'no delevery')], default='no delivery', max_length=50),
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='done_purchases', to='profiles.profile')),
            ],
        ),
    ]
