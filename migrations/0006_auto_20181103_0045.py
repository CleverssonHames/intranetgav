# Generated by Django 2.0.1 on 2018-11-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0005_auto_20181029_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeptosFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome do arquivo')),
                ('descricao', models.TextField(verbose_name='descriçao do arquivo')),
                ('arquivo', models.FileField(upload_to='media')),
                ('depto', models.CharField(choices=[('1', 'RH'), ('2', 'Dpto. Pessoal'), ('3', 'Jurido'), ('4', 'Financeiro'), ('5', 'Fiscal'), ('6', 'Contabilidade'), ('7', 'Compras'), ('8', 'Auditoria'), ('9', 'MKT'), ('10', 'Compras Indiretas'), ('11', 'Patrimonio'), ('12', 'TI')], max_length=2, verbose_name='Departamento')),
            ],
        ),
        migrations.AlterField(
            model_name='linksites',
            name='local',
            field=models.CharField(choices=[('L', 'Loja'), ('E', 'Escrtorio')], max_length=1, verbose_name='local'),
        ),
        migrations.AlterField(
            model_name='linksites',
            name='site',
            field=models.CharField(max_length=50, verbose_name='site'),
        ),
        migrations.AlterField(
            model_name='linksites',
            name='tipo_acesso',
            field=models.CharField(choices=[('I', 'Interno'), ('E', 'Externo'), ('IE', 'Interno/Externo')], max_length=2, verbose_name='tipo acesso'),
        ),
        migrations.AlterField(
            model_name='linksites',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='titulo'),
        ),
    ]
