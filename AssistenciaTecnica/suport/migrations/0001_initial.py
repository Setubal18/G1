# Generated by Django 2.0.2 on 2018-04-02 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('telefone', models.CharField(max_length=50)),
                ('data', models.DateField(verbose_name='Data da Abertura da chamada')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suport.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Chamadas',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suport.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='FuncionarioSuporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('especializacao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('feminino', 'Feminino'), ('masculino', 'Masculino')], max_length=10)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(max_length=13)),
                ('tell', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='funcionariosuporte',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suport.Pessoa'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suport.Pessoa'),
        ),
        migrations.AddField(
            model_name='chamada',
            name='Departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suport.Departamento'),
        ),
        migrations.AddField(
            model_name='chamada',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suport.Status'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='atendimento',
            field=models.ManyToManyField(to='suport.FuncionarioSuporte'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='chamada',
            field=models.ManyToManyField(to='suport.Chamada'),
        ),
    ]