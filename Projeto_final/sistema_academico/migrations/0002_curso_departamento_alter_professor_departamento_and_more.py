# Generated by Django 5.0.2 on 2024-03-12 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_academico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sistema_academico.departamento'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_academico.departamento'),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='sistema_academico.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_academico.curso')),
            ],
        ),
    ]
