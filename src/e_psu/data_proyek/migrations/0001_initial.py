# Generated by Django 3.1 on 2020-09-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SerahTerima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokasi_proyek', models.CharField(blank=True, max_length=255)),
                ('luas_total_area_proyek', models.FloatField()),
                ('jumlah_total_unit', models.IntegerField()),
                ('jenis_produk', models.CharField(blank=True, max_length=50)),
                ('jumlah_tipe_rumah', models.IntegerField()),
                ('target_pembangunan', models.IntegerField()),
                ('verified_tipe_rumah', models.BooleanField()),
                ('verified_jenis_psu', models.BooleanField()),
                ('verified_data_perizinan', models.BooleanField()),
                ('verified_admin_data_proyek', models.PositiveSmallIntegerField()),
                ('verified_admin_tipe_rumah', models.PositiveSmallIntegerField()),
                ('verified_admin_jenis_psu', models.PositiveSmallIntegerField()),
                ('verified_admin_data_perizinan', models.PositiveSmallIntegerField()),
                ('id_data_perusahaan_id', models.IntegerField()),
            ],
            options={
                'db_table': 'pelaporan_dataproyek',
            },
        ),
    ]
