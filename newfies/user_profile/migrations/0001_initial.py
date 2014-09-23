# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_lets_go.language_field
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dialer_settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dialer_gateway', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, null=True, verbose_name='address', blank=True)),
                ('city', models.CharField(max_length=120, null=True, verbose_name='city', blank=True)),
                ('state', models.CharField(max_length=120, null=True, verbose_name='state', blank=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='country', choices=[('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia, Plurinational State of'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo (the Democratic Republic of the)'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Cura\xe7ao'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('CI', "C\xf4te d'Ivoire"), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands  [Malvinas]'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia (The)'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See  [Vatican City State]'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran (the Islamic Republic of)'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea (the Democratic People's Republic of)"), ('KR', 'Korea (the Republic of)'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia (the Federated States of)'), ('MD', 'Moldova (the Republic of)'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine, State of'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('RE', 'R\xe9union'), ('BL', 'Saint Barth\xe9lemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan (Province of China)'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands (British)'), ('VI', 'Virgin Islands (U.S.)'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'), ('AX', '\xc5land Islands')])),
                ('zip_code', models.CharField(max_length=120, null=True, verbose_name='zip code', blank=True)),
                ('phone_no', models.CharField(max_length=90, null=True, verbose_name='phone number', blank=True)),
                ('fax', models.CharField(max_length=90, null=True, verbose_name='fax Number', blank=True)),
                ('company_name', models.CharField(max_length=90, null=True, verbose_name='company name', blank=True)),
                ('company_website', models.URLField(max_length=90, null=True, verbose_name='company website', blank=True)),
                ('language', django_lets_go.language_field.LanguageField(blank=True, max_length=2, null=True, verbose_name='language', choices=[(b'aa', 'Afar'), (b'ab', 'Abkhazian'), (b'af', 'Afrikaans'), (b'ak', 'Akan'), (b'sq', 'Albanian'), (b'am', 'Amharic'), (b'ar', 'Arabic'), (b'an', 'Aragonese'), (b'hy', 'Armenian'), (b'as', 'Assamese'), (b'av', 'Avaric'), (b'ae', 'Avestan'), (b'ay', 'Aymara'), (b'az', 'Azerbaijani'), (b'ba', 'Bashkir'), (b'bm', 'Bambara'), (b'eu', 'Basque'), (b'be', 'Belarusian'), (b'bn', 'Bengali'), (b'bh', 'Bihari languages'), (b'bi', 'Bislama'), (b'bo', 'Tibetan'), (b'bs', 'Bosnian'), (b'br', 'Breton'), (b'bg', 'Bulgarian'), (b'my', 'Burmese'), (b'ca', 'Catalan; Valencian'), (b'cs', 'Czech'), (b'ch', 'Chamorro'), (b'ce', 'Chechen'), (b'zh', 'Chinese'), (b'cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'), (b'cv', 'Chuvash'), (b'kw', 'Cornish'), (b'co', 'Corsican'), (b'cr', 'Cree'), (b'cy', 'Welsh'), (b'cs', 'Czech'), (b'da', 'Danish'), (b'de', 'German'), (b'dv', 'Divehi; Dhivehi; Maldivian'), (b'nl', 'Dutch; Flemish'), (b'dz', 'Dzongkha'), (b'el', 'Greek, Modern (1453-)'), (b'en', 'English'), (b'eo', 'Esperanto'), (b'et', 'Estonian'), (b'eu', 'Basque'), (b'ee', 'Ewe'), (b'fo', 'Faroese'), (b'fa', 'Persian'), (b'fj', 'Fijian'), (b'fi', 'Finnish'), (b'fr', 'French'), (b'fr', 'French'), (b'fy', 'Western Frisian'), (b'ff', 'Fulah'), (b'ka', 'Georgian'), (b'de', 'German'), (b'gd', 'Gaelic; Scottish Gaelic'), (b'ga', 'Irish'), (b'gl', 'Galician'), (b'gv', 'Manx'), (b'el', 'Greek, Modern (1453-)'), (b'gn', 'Guarani'), (b'gu', 'Gujarati'), (b'ht', 'Haitian; Haitian Creole'), (b'ha', 'Hausa'), (b'he', 'Hebrew'), (b'hz', 'Herero'), (b'hi', 'Hindi'), (b'ho', 'Hiri Motu'), (b'hr', 'Croatian'), (b'hu', 'Hungarian'), (b'hy', 'Armenian'), (b'ig', 'Igbo'), (b'is', 'Icelandic'), (b'io', 'Ido'), (b'ii', 'Sichuan Yi; Nuosu'), (b'iu', 'Inuktitut'), (b'ie', 'Interlingue; Occidental'), (b'ia', 'Interlingua (International Auxiliary Language Association)'), (b'id', 'Indonesian'), (b'ik', 'Inupiaq'), (b'is', 'Icelandic'), (b'it', 'Italian'), (b'jv', 'Javanese'), (b'ja', 'Japanese'), (b'kl', 'Kalaallisut; Greenlandic'), (b'kn', 'Kannada'), (b'ks', 'Kashmiri'), (b'ka', 'Georgian'), (b'kr', 'Kanuri'), (b'kk', 'Kazakh'), (b'km', 'Central Khmer'), (b'ki', 'Kikuyu; Gikuyu'), (b'rw', 'Kinyarwanda'), (b'ky', 'Kirghiz; Kyrgyz'), (b'kv', 'Komi'), (b'kg', 'Kongo'), (b'ko', 'Korean'), (b'kj', 'Kuanyama; Kwanyama'), (b'ku', 'Kurdish'), (b'lo', 'Lao'), (b'la', 'Latin'), (b'lv', 'Latvian'), (b'li', 'Limburgan; Limburger; Limburgish'), (b'ln', 'Lingala'), (b'lt', 'Lithuanian'), (b'lb', 'Luxembourgish; Letzeburgesch'), (b'lu', 'Luba-Katanga'), (b'lg', 'Ganda'), (b'mk', 'Macedonian'), (b'mh', 'Marshallese'), (b'ml', 'Malayalam'), (b'mi', 'Maori'), (b'mr', 'Marathi'), (b'ms', 'Malay'), (b'mk', 'Macedonian'), (b'mg', 'Malagasy'), (b'mt', 'Maltese'), (b'mn', 'Mongolian'), (b'mi', 'Maori'), (b'ms', 'Malay'), (b'my', 'Burmese'), (b'na', 'Nauru'), (b'nv', 'Navajo; Navaho'), (b'nr', 'Ndebele, South; South Ndebele'), (b'nd', 'Ndebele, North; North Ndebele'), (b'ng', 'Ndonga'), (b'ne', 'Nepali'), (b'nl', 'Dutch; Flemish'), (b'nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'), (b'nb', 'Bokmal, Norwegian; Norwegian Bokmal'), (b'no', 'Norwegian'), (b'ny', 'Chichewa; Chewa; Nyanja'), (b'oc', 'Occitan (post 1500)'), (b'oj', 'Ojibwa'), (b'or', 'Oriya'), (b'om', 'Oromo'), (b'os', 'Ossetian; Ossetic'), (b'pa', 'Panjabi; Punjabi'), (b'fa', 'Persian'), (b'pi', 'Pali'), (b'pl', 'Polish'), (b'pt', 'Portuguese'), (b'ps', 'Pushto; Pashto'), (b'qu', 'Quechua'), (b'rm', 'Romansh'), (b'ro', 'Romanian; Moldavian; Moldovan'), (b'ro', 'Romanian; Moldavian; Moldovan'), (b'rn', 'Rundi'), (b'ru', 'Russian'), (b'sg', 'Sango'), (b'sa', 'Sanskrit'), (b'si', 'Sinhala; Sinhalese'), (b'sk', 'Slovak'), (b'sk', 'Slovak'), (b'sl', 'Slovenian'), (b'se', 'Northern Sami'), (b'sm', 'Samoan'), (b'sn', 'Shona'), (b'sd', 'Sindhi'), (b'so', 'Somali'), (b'st', 'Sotho, Southern'), (b'es', 'Spanish; Castilian'), (b'sq', 'Albanian'), (b'sc', 'Sardinian'), (b'sr', 'Serbian'), (b'ss', 'Swati'), (b'su', 'Sundanese'), (b'sw', 'Swahili'), (b'sv', 'Swedish'), (b'ty', 'Tahitian'), (b'ta', 'Tamil'), (b'tt', 'Tatar'), (b'te', 'Telugu'), (b'tg', 'Tajik'), (b'tl', 'Tagalog'), (b'th', 'Thai'), (b'bo', 'Tibetan'), (b'ti', 'Tigrinya'), (b'to', 'Tonga (Tonga Islands)'), (b'tn', 'Tswana'), (b'ts', 'Tsonga'), (b'tk', 'Turkmen'), (b'tr', 'Turkish'), (b'tw', 'Twi'), (b'ug', 'Uighur; Uyghur'), (b'uk', 'Ukrainian'), (b'ur', 'Urdu'), (b'uz', 'Uzbek'), (b've', 'Venda'), (b'vi', 'Vietnamese'), (b'vo', 'Volapuk'), (b'cy', 'Welsh'), (b'wa', 'Walloon'), (b'wo', 'Wolof'), (b'xh', 'Xhosa'), (b'yi', 'Yiddish'), (b'yo', 'Yoruba'), (b'za', 'Zhuang; Chuang'), (b'zh', 'Chinese'), (b'zu', 'Zulu')])),
                ('note', models.CharField(max_length=250, null=True, verbose_name='note', blank=True)),
                ('accountcode', models.PositiveIntegerField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('dialersetting', models.ForeignKey(verbose_name='dialer settings', blank=True, to='dialer_settings.DialerSetting', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userprofile_gateway', models.ManyToManyField(to='dialer_gateway.Gateway', verbose_name='gateway')),
            ],
            options={
                'db_table': 'user_profile',
                'verbose_name': 'user profile',
                'verbose_name_plural': 'user profiles',
                'permissions': (('view_api_explorer', 'can see API-Explorer'),),
            },
            bases=(models.Model,),
        ),
    ]
