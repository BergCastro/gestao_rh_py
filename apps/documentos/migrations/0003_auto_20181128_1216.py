# Generated by Django 2.1 on 2018-11-28 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documento_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]
