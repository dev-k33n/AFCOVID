# Generated by Django 3.2.5 on 2021-07-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserData', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': 'หน่วยขึ้นตรง ทอ. [Unit]'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('User_AF_CMO', 'User AF CMO'), ('User_Unit_CMO', 'User Unit CMO'), ('User_PMD', 'User PMD'), ('User_CRC', 'User CRC'))},
        ),
        migrations.AddField(
            model_name='unit',
            name='FullName',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='unit',
            name='ShortName',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='MobileTel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='OfficePhone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Position',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Rank',
            field=models.PositiveIntegerField(choices=[(30101, 'พล.อ.อ.*'), (30102, 'พล.อ.อ.*หญิง'), (30211, 'พล.อ.อ.'), (30212, 'พล.อ.อ.หญิง'), (30221, 'พล.อ.ท.'), (30222, 'พล.อ.ท.หญิง'), (30231, 'พล.อ.ต.'), (30232, 'พล.อ.ต.หญิง'), (30301, 'น.อ.(พ)'), (30302, 'น.อ.(พ) หญิง'), (30411, 'น.อ.'), (30412, 'น.อ.หญิง'), (30421, 'น.ท.'), (30422, 'น.ท.หญิง'), (30431, 'น.ต.'), (30432, 'น.ต.หญิง'), (30511, 'ร.อ.'), (30512, 'ร.อ.หญิง'), (30521, 'ร.ท.'), (30522, 'ร.ท.หญิง'), (30531, 'ร.ต.'), (30532, 'ร.ต.หญิง'), (30541, 'กห.ส.'), (30542, 'กห.ส.หญิง'), (30611, 'พ.อ.อ.(พ)'), (30612, 'พ.อ.อ.(พ) หญิง'), (30711, 'พ.อ.อ.'), (30712, 'พ.อ.อ.หญิง'), (30721, 'พ.อ.ท.'), (30722, 'พ.อ.ท.หญิง'), (30731, 'พ.อ.ต.'), (30732, 'พ.อ.ต.หญิง'), (30811, 'จ.อ.'), (30812, 'จ.อ.หญิง'), (30821, 'จ.ท.'), (30822, 'จ.ท.หญิง'), (30831, 'จ.ท.'), (30832, 'จ.ต.หญิง'), (30841, 'กห.ป.'), (30842, 'กห.ป.หญิง'), (31411, 'ว่าที่ น.อ.'), (31412, 'ว่าที่ น.อ.หญิง'), (31421, 'ว่าที่ น.ท.'), (31422, 'ว่าที่ น.ท.หญิง'), (31431, 'ว่าที่ น.ต.'), (31432, 'ว่าที่ น.ต.หญิง'), (31511, 'ว่าที่ ร.อ.'), (31512, 'ว่าที่ ร.อ.หญิง'), (31521, 'ว่าที่ ร.ท.'), (31522, 'ว่าที่ ร.ท.หญิง'), (31531, 'ว่าที่ ร.ต.'), (31532, 'ว่าที่ ร.ต.หญิง'), (40200, 'พนง.อาวุโสหญิง'), (40201, 'พนง.อาวุโส'), (40400, 'พนง.หญิง'), (40401, 'พนง.'), (50000, '----')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Unit',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]