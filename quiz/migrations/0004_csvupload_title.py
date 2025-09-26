from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_csvupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvupload',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
