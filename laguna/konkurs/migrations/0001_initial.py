# Generated by Django 2.0 on 2017-12-14 16:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import konkurs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Autor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Uczestnik',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, validators=[django.core.validators.EmailValidator()])),
                ('firstname', models.CharField(max_length=50, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=50, verbose_name='Lastname')),
                ('birthday', models.DateField(validators=[konkurs.models.MinAgeValidator(18)])),
                ('place_of_birth', models.CharField(default='Kalisz', max_length=30, verbose_name='Place Of Birth')),
                ('alias', models.CharField(max_length=50, verbose_name='Alias')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('cellphone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('nationality', models.CharField(choices=[('Afghanistan', 'Afganistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('America', 'Ameryka'), ('Andorra', 'Andora'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Argentina', 'Argentyna'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijani'), ('the Bahamas', 'Bahamy'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesz'), ('Barbados', 'Barbados'), ('Barbudans', 'Barbudany'), ('Botswana', 'Botswana'), ('Belarus', 'Białoruś'), ('Belgium', 'Belgia'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Boliwia'), ('Bosnia', 'Bośnia'), ('Brazylia', 'Brazylia'), ('Britain', 'Wielka Brytania'), ('Bruneia', 'Bruneia'), ('Bulgaria', 'Bułgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burma', 'Birma'), ('Burgundia', 'Burgundia'), ('Cambodia', 'Kambodża'), ('Cameroon', 'Kamerun'), ('Canada', 'Kanada'), ('Cape Verde', 'Republika Zielonego Przylądka'), ('Central Africa', 'Centralna Afryka'), ('Chad', 'Czad'), ('Chile', 'Chile'), ('China', 'Chiny'), ('Colombia', 'Kolumbia'), ('Camorra', 'Camorra'), ('Democratic Republic of the Congo', 'Demokratyczna Republika Konga'), ('Costa Rica', 'Kostaryka'), ('Croatia', 'Chorwacja'), ('Cuba', 'Kuba'), ('Cyprus', 'Cypr'), ('Czechia', 'Czechy'), ('Denmark', 'Dania'), ('Djibouti', 'Dżibuti'), ('Dominica', 'Dominika'), ('Holland', 'Holandia'), ('East Timor', 'Wschodni Timor'), ('Ecuador', 'Ekwador'), ('Egypt', 'Egipt'), ('United Arab Emirates', 'Zjednoczone Emiraty Arabskie'), ('Equatorial Guinea', 'Ginea Równikowa'), ('Eritrea', 'Erytrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Etiopia'), ('Fiji', 'Fidżi'), ('Philippines', 'Filipiny'), ('Finn', 'Finy'), ('France', 'Francja'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Gruzja'), ('Germany', 'Niemcy'), ('Ghana', 'Ghana'), ('Greece', 'Grecja'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea-Bissau', 'Gwinea Bissau'), ('Guinea', 'Gwinea'), ('Guyana', 'Gujana'), ('Haiti', 'Haiti'), ('Herzegovina', 'Hercegowina'), ('Honduras', 'Honduras'), ('Hungary', 'Węgry'), ('Iceland', 'Islandia'), ('India', 'Indie'), ('Indonesia', 'Indonezja'), ('Iran', 'Iran'), ('Iraq', 'Irak'), ('Ireland', 'Irlandia'), ('Israel', 'Izrael'), ('Italy', 'Włochy'), ('Ivory Coast', 'Wybrzeże Kości Słoniowej'), ('Jamaica', 'Jamajka'), ('Japan', 'Japonia'), ('Jordan', 'Jordania'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenia'), ('Kittian and Nevisian', 'Kittan and Nevisian'), ('Kuwait', 'Kuwejt'), ('Kyrgyzstan', 'Kirgistan'), ('Lao', 'Laos'), ('Latvia', 'Łotwa'), ('Lebanon', 'Liban'), ('Liberia', 'Liberia'), ('Libya', 'Libia'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Litwa'), ('Luxembourg', 'Luksemburg'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagaskar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malezja'), ('Maldives', 'Malediwy'), ('Malia', 'Malia'), ('Malaysia', 'Malezja'), ('the Marshall Islands', 'Wyspy Marshalla'), ('Mauritania', 'Mauretania'), ('Mexic', 'Meksyk'), ('Micronesia', 'Mikronezja'), ('Moldova', 'Mołdawia'), ('Monaco', 'Monako'), ('Mongolia', 'Mongolia'), ('Morocco', 'Maroko'), ('Lesotho', 'Lesotho'), ('Mozambique', 'Mozambik'), ('Namibia', 'Namibia'), ('Nauruan', 'Republika Nauru'), ('Nepal', 'Nepal'), ('New Zealand', 'Nowa Zelandia'), ('Nicaragua', 'Nikaragua'), ('Nigeria', 'Nigeria'), ('North Korea', 'Korea Północna'), ('Norway', 'Norwegia'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua Nowa Gwinea'), ('Paraguay', 'Paragwaj'), ('Peru', 'Peru'), ('Poland', 'Polska'), ('Portugal', 'Portugalia'), ('Qatar', 'Katar'), ('Romania', 'Rumunia'), ('Russia', 'Rosja'), ('Rwanda', 'Rwanda'), ('Saint Lucia', 'Saint Lucia'), ('Salvador', 'Salwador'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Saudi Arabia', 'Arabia Saudyjska'), ('Scotland', 'Szkocja'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seszele'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapur'), ('Slovakia', 'Słowacja'), ('Slovenia', 'Słowenia'), ('Solomon Island', 'Wyspa Salomona'), ('Somalia', 'Somalia'), ('South Africa', 'Połódniowa Afryka'), ('South Korea', 'Połódniowa Korea'), ('Spain', 'Hiszpania'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Surinam', 'Surinam'), ('Swaziland', 'Suazi'), ('Sweden', 'Szwecja'), ('Switzerland', 'Szwajcaria'), ('Syria', 'Syria'), ('Taiwan', 'Tajwan'), ('Tajikistan', 'Tadżykistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Tajlandia'), ('Togo', 'Togo'), ('Tonga', 'Tongo'), ('Tobago', 'Tobago'), ('Trinidad', 'Trynidad'), ('Tunisia', 'Tunezja'), ('Turkey', 'Turcja'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraina', 'Ukraine'), ('Uruguay', 'Urugwaj'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Wenezuela'), ('Vietnam', 'Wietnam'), ('Wales', 'Walia'), ('Yemen', 'Jemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=30)),
                ('biography', models.TextField()),
                ('country', models.CharField(choices=[('Afghanistan', 'Afganistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('America', 'Ameryka'), ('Andorra', 'Andora'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Argentina', 'Argentyna'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijani'), ('the Bahamas', 'Bahamy'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesz'), ('Barbados', 'Barbados'), ('Barbudans', 'Barbudany'), ('Botswana', 'Botswana'), ('Belarus', 'Białoruś'), ('Belgium', 'Belgia'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Boliwia'), ('Bosnia', 'Bośnia'), ('Brazylia', 'Brazylia'), ('Britain', 'Wielka Brytania'), ('Bruneia', 'Bruneia'), ('Bulgaria', 'Bułgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burma', 'Birma'), ('Burgundia', 'Burgundia'), ('Cambodia', 'Kambodża'), ('Cameroon', 'Kamerun'), ('Canada', 'Kanada'), ('Cape Verde', 'Republika Zielonego Przylądka'), ('Central Africa', 'Centralna Afryka'), ('Chad', 'Czad'), ('Chile', 'Chile'), ('China', 'Chiny'), ('Colombia', 'Kolumbia'), ('Camorra', 'Camorra'), ('Democratic Republic of the Congo', 'Demokratyczna Republika Konga'), ('Costa Rica', 'Kostaryka'), ('Croatia', 'Chorwacja'), ('Cuba', 'Kuba'), ('Cyprus', 'Cypr'), ('Czechia', 'Czechy'), ('Denmark', 'Dania'), ('Djibouti', 'Dżibuti'), ('Dominica', 'Dominika'), ('Holland', 'Holandia'), ('East Timor', 'Wschodni Timor'), ('Ecuador', 'Ekwador'), ('Egypt', 'Egipt'), ('United Arab Emirates', 'Zjednoczone Emiraty Arabskie'), ('Equatorial Guinea', 'Ginea Równikowa'), ('Eritrea', 'Erytrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Etiopia'), ('Fiji', 'Fidżi'), ('Philippines', 'Filipiny'), ('Finn', 'Finy'), ('France', 'Francja'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Gruzja'), ('Germany', 'Niemcy'), ('Ghana', 'Ghana'), ('Greece', 'Grecja'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea-Bissau', 'Gwinea Bissau'), ('Guinea', 'Gwinea'), ('Guyana', 'Gujana'), ('Haiti', 'Haiti'), ('Herzegovina', 'Hercegowina'), ('Honduras', 'Honduras'), ('Hungary', 'Węgry'), ('Iceland', 'Islandia'), ('India', 'Indie'), ('Indonesia', 'Indonezja'), ('Iran', 'Iran'), ('Iraq', 'Irak'), ('Ireland', 'Irlandia'), ('Israel', 'Izrael'), ('Italy', 'Włochy'), ('Ivory Coast', 'Wybrzeże Kości Słoniowej'), ('Jamaica', 'Jamajka'), ('Japan', 'Japonia'), ('Jordan', 'Jordania'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenia'), ('Kittian and Nevisian', 'Kittan and Nevisian'), ('Kuwait', 'Kuwejt'), ('Kyrgyzstan', 'Kirgistan'), ('Lao', 'Laos'), ('Latvia', 'Łotwa'), ('Lebanon', 'Liban'), ('Liberia', 'Liberia'), ('Libya', 'Libia'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Litwa'), ('Luxembourg', 'Luksemburg'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagaskar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malezja'), ('Maldives', 'Malediwy'), ('Malia', 'Malia'), ('Malaysia', 'Malezja'), ('the Marshall Islands', 'Wyspy Marshalla'), ('Mauritania', 'Mauretania'), ('Mexic', 'Meksyk'), ('Micronesia', 'Mikronezja'), ('Moldova', 'Mołdawia'), ('Monaco', 'Monako'), ('Mongolia', 'Mongolia'), ('Morocco', 'Maroko'), ('Lesotho', 'Lesotho'), ('Mozambique', 'Mozambik'), ('Namibia', 'Namibia'), ('Nauruan', 'Republika Nauru'), ('Nepal', 'Nepal'), ('New Zealand', 'Nowa Zelandia'), ('Nicaragua', 'Nikaragua'), ('Nigeria', 'Nigeria'), ('North Korea', 'Korea Północna'), ('Norway', 'Norwegia'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua Nowa Gwinea'), ('Paraguay', 'Paragwaj'), ('Peru', 'Peru'), ('Poland', 'Polska'), ('Portugal', 'Portugalia'), ('Qatar', 'Katar'), ('Romania', 'Rumunia'), ('Russia', 'Rosja'), ('Rwanda', 'Rwanda'), ('Saint Lucia', 'Saint Lucia'), ('Salvador', 'Salwador'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Saudi Arabia', 'Arabia Saudyjska'), ('Scotland', 'Szkocja'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seszele'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapur'), ('Slovakia', 'Słowacja'), ('Slovenia', 'Słowenia'), ('Solomon Island', 'Wyspa Salomona'), ('Somalia', 'Somalia'), ('South Africa', 'Połódniowa Afryka'), ('South Korea', 'Połódniowa Korea'), ('Spain', 'Hiszpania'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Surinam', 'Surinam'), ('Swaziland', 'Suazi'), ('Sweden', 'Szwecja'), ('Switzerland', 'Szwajcaria'), ('Syria', 'Syria'), ('Taiwan', 'Tajwan'), ('Tajikistan', 'Tadżykistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Tajlandia'), ('Togo', 'Togo'), ('Tonga', 'Tongo'), ('Tobago', 'Tobago'), ('Trinidad', 'Trynidad'), ('Tunisia', 'Tunezja'), ('Turkey', 'Turcja'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraina', 'Ukraine'), ('Uruguay', 'Urugwaj'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Wenezuela'), ('Vietnam', 'Wietnam'), ('Wales', 'Walia'), ('Yemen', 'Jemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=30)),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('street_line', models.CharField(blank=True, max_length=100, verbose_name='Address')),
                ('site', models.CharField(max_length=50)),
                ('zipcode', models.CharField(blank=True, max_length=5, verbose_name='ZIP code')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DigitalGraphic',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('obraz', models.ImageField(upload_to='')),
                ('opis', models.TextField()),
                ('cena', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='LandArt',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('obraz1', models.ImageField(upload_to='')),
                ('obraz2', models.ImageField(upload_to='')),
                ('obraz3', models.ImageField(upload_to='')),
                ('opis', models.TextField()),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('wymiary', models.CharField(max_length=10)),
                ('opis', models.TextField()),
                ('cena', models.CharField(max_length=10)),
                ('obraz', models.ImageField(upload_to='')),
                ('technika', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='Performence',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=20)),
                ('opis', models.TextField()),
                ('cena', models.CharField(max_length=10)),
                ('obraz', models.ImageField(upload_to='')),
                ('year', models.IntegerField()),
                ('video_url', models.URLField()),
                ('video_password', models.CharField(max_length=50)),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('wymiary', models.CharField(max_length=10)),
                ('opis', models.TextField()),
                ('cena', models.CharField(max_length=10)),
                ('obraz', models.ImageField(upload_to='')),
                ('technika', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='Sculpture',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('wymiary', models.CharField(max_length=30)),
                ('opis', models.TextField()),
                ('cena', models.CharField(max_length=10)),
                ('obraz1', models.ImageField(upload_to='')),
                ('obraz2', models.ImageField(upload_to='')),
                ('obraz3', models.ImageField(upload_to='')),
                ('video_url', models.URLField()),
                ('video_password', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='UrbanArt',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('obraz1', models.ImageField(upload_to='')),
                ('obraz2', models.ImageField(upload_to='')),
                ('obraz3', models.ImageField(upload_to='')),
                ('opis', models.TextField()),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=20)),
                ('opis', models.TextField()),
                ('cena', models.CharField(max_length=10)),
                ('obraz', models.ImageField(upload_to='')),
                ('year', models.IntegerField()),
                ('video_url', models.URLField()),
                ('video_password', models.CharField(max_length=50)),
            ],
            bases=('konkurs.work',),
        ),
        migrations.CreateModel(
            name='VirtualArt',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='konkurs.Work')),
                ('title', models.CharField(max_length=30)),
                ('wymiary', models.CharField(max_length=10)),
                ('opis', models.TextField()),
                ('cena', models.CharField(max_length=10)),
                ('obraz1', models.ImageField(upload_to='')),
                ('obraz2', models.ImageField(upload_to='')),
                ('obraz3', models.ImageField(upload_to='')),
                ('video_url', models.URLField()),
                ('video_password', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
            bases=('konkurs.work',),
        ),
        migrations.AddField(
            model_name='work',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konkurs.Uczestnik'),
        ),
        migrations.AddField(
            model_name='work',
            name='reviews',
            field=models.ManyToManyField(through='konkurs.Review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='konkurs.Work'),
        ),
    ]
